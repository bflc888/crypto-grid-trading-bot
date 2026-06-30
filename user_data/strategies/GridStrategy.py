from freqtrade.strategy import IStrategy
from pandas import DataFrame
import talib.abstract as ta
from datetime import timedelta

class GridStrategy(IStrategy):
    """
    网格交易策略 - 自动高抛低吸
    """
    INTERFACE_VERSION = 3
    
    # 买入信号参数
    minimal_roi = {
        "0": 0.10  # 目标收益 10%
    }
    
    # 止损
    stoploss = -0.05  # 止损 5%
    
    # 时间框架
    timeframe = '5m'
    
    # 交易对
    can_short = False
    
    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        计算技术指标
        """
        # 计算 RSI
        dataframe['rsi'] = ta.RSI(dataframe, timeperiod=14)
        
        # 计算移动平均线
        dataframe['sma_20'] = ta.SMA(dataframe, timeperiod=20)
        dataframe['sma_50'] = ta.SMA(dataframe, timeperiod=50)
        
        # 计算 Bollinger Band（布林带）
        dataframe['bb_lower'] = ta.BBANDS(dataframe, timeperiod=20, nbdevup=2, nbdevdn=2)[0]
        dataframe['bb_middle'] = ta.BBANDS(dataframe, timeperiod=20, nbdevup=2, nbdevdn=2)[1]
        dataframe['bb_upper'] = ta.BBANDS(dataframe, timeperiod=20, nbdevup=2, nbdevdn=2)[2]
        
        return dataframe
    
    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        网格买入信号 - 价格触及下轨时买入
        """
        dataframe.loc[
            (
                (dataframe['close'] < dataframe['bb_lower']) &  # 价格低于布林带下轨
                (dataframe['rsi'] < 30) &  # RSI 超卖
                (dataframe['volume'] > 0)
            ),
            'enter_long'] = 1
        
        return dataframe
    
    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        网格卖出信号 - 价格触及上轨时卖出
        """
        dataframe.loc[
            (
                (dataframe['close'] > dataframe['bb_upper']) |  # 价格高于布林带上轨
                (dataframe['rsi'] > 70)  # RSI 超买
            ),
            'exit_long'] = 1
        
        return dataframe