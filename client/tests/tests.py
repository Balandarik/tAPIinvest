import unittest
from client.tAPIinvest import *
token = 'test'


class Tests(unittest.TestCase):
    
    def setUp(self):
        self.function = main_function(token)
        self.sandbox = Sandbox(token)
        
    def test_bonds(self):
        self.assertEqual('Authentication failed',self.function.bonds()['message'])
        
    def test_currencieBy(self):
        self.assertEqual('Authentication failed',self.function.currencieBy(figi='BBG0013J12N1')['message'])
        
    def test_GetAccruedInterests(self):
        self.assertEqual('Authentication failed',self.function.GetAccruedInterests(figi='BBG011MDDX15',_from='2021-08-20T07:02:09.881Z',_to='2022-01-20T07:02:09.881Z')['message'])
   
    
    def test_GetFuturesMargin(self):
        self.assertEqual('Authentication failed', self.function.GetFuturesMargin(figi='FUTMOEX03220')['message'])
       
        
    def test_GetInstrumentBy(self):
        self.assertEqual('Authentication failed',self.function.GetInstrumentBy(figi='FUTMOEX03220')['message'])
        

    def test_GetAccounts(self):
        self.assertEqual('Authentication failed',self.function.GetAccounts()['message'])
        
        
    def test_GetInfo(self):
        self.assertEqual('Authentication failed',self.function.GetInfo()['message'])
      
        
    def test_GetUserTariff(self):
        self.assertEqual('Authentication failed',self.function.GetUserTariff()['message'])
        

    def test_GetCandles(self):
        self.assertEqual('Authentication failed',self.function.GetCandles('BBG000C0HQ54','2022-01-19T19:54:37.444Z','2022-01-20T16:54:37.444Z')['message'])
        

    def test_LasPrices(self):
        self.assertEqual(None,self.function.GetLastPrices(['BBG000C0HQ54','BBG00GNC8DL2'])['message'])
        self.assertEqual(None,self.function.GetLastPrices('BBG000C0HQ54')['message'])
        
    def test_GetOrderBook(self):
        self.assertEqual('Authentication failed',self.function.GetOrderBook('BBG000C0HQ54')['message'])

    def test_GetTradingStatus(self):
        self.assertEqual('Authentication failed',self.function.GetTradingStatus('BBG000C0HQ54')['message'])
      
    def test_GetPortfolio(self):
        self.assertEqual('Authentication failed',self.function.GetPortfolio('345345345')['message'])

    def test_GetPositions(self):
        self.assertEqual('Authentication failed',self.function.GetPositions('345345345345')['message'])
        
    def test_GetWithdrawLimits(self):
        self.assertEqual('Authentication failed',self.function.GetWithdrawLimits('345345345345')['message'])


    def test_GetOperations(self):
        self.assertEqual('Authentication failed',self.function.GetOperation('345354534534','2022-01-05T19:54:37.444Z','2022-01-20T16:54:37.444Z','FUTSBPR06220')['message'])

    def test_GetOrders(self):
        self.assertEqual('Authentication failed',self.function.GetOrders('345345345')['message'])

    def test_CancelOrder(self):
        self.assertEqual('Authentication failed',self.function.CancelOrder('209745345333458','53453453')['message'])

    def test_GetOrderState(self):
        self.assertEqual('Authentication failed',self.function.GetOrderState('5345345','543')['message'])

    def test_GetStopOrders(self):
        self.assertEqual('Authentication failed',self.function.GetStopOrders('3423423')['message'])

    def test_CancelStopOrder(self):
        self.assertEqual('Authentication failed',self.function.CancelStopOrder('23423423','234')['message'])
        
    def test_GetStopOrders(self):
        self.assertEqual('Authentication failed',self.function.GetStopOrders('23423423')['message'])
        
    def test_CancelSandboxOrder(self):
        self.assertEqual('Authentication failed',self.sandbox.CancelSandboxOrder('209745345333458','53453453')['message'])
        
    def test_GetSandboxAccounts(self):
        self.assertEqual('Authentication failed',self.sandbox.GetSandboxAccounts()['message'])
        
    def test_GetSandboxOperations(self):
        self.assertEqual('Authentication failed',self.sandbox.GetSandboxOperations('345354534534','2022-01-05T19:54:37.444Z','2022-01-20T16:54:37.444Z','FUTSBPR06220')['message'])

    def test_GetSandboxPortfolio(self):
        self.assertEqual('Authentication failed',self.sandbox.GetSandboxPortfolio('345345345')['message'])
        
    def test_GetSandboxPositions(self):
        self.assertEqual('Authentication failed',self.sandbox.GetSandboxPositions('345345345345')['message'])
        
    def test_OpenSandboxAccount(self):
        self.assertEqual('Authentication failed',self.sandbox.OpenSandboxAccount()['message'])
        
    def test_CloseSandboxAccount(self):
        self.assertEqual('Authentication failed',self.sandbox.CloseSandboxAccount('209745345333458')['message'])
               
def start_tests():
    unittest.main()