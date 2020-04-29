import pytest

# Import webdriver for automation
from selenium import webdriver
import openpyxl

# Importing the ChromeDriver class for handling webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Commons import Constants, XLUtils
from Commons.login import MainLogin_Test
from Test.Resource_Customer import TestCustomer1
from Test.Resource_Provider import TestProvider1
from Test.L1L_Facility import TestFacility
from Test.Configuration_View import TestView1
from Test.L1S_Circuit import TestCircuit


class TestMain:
    url = "http://192.168.221.253:8180/tnp-inventory"

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())  # diver
        # self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get(self.url)

    def test_TestCase(self, setup):
        try:
            a = MainLogin_Test(self.driver).Login_Test()

            if a:
                # To Avoid the interpretation of escape characters. raw strings('r') is used in front
                path = r"../FileReference/TR1-CMP-TST01-INV-MIV-L1S-LAYER1-001_00001-001_00005 vs 1.0 - GUI Automation.xlsx"

                workbook = openpyxl.load_workbook(path)

                Sheet = workbook['GUI Automation']

                rows = XLUtils.getRowCount(path, Sheet.title)

                for r in range(2, rows + 1):
                    TestCaseId = XLUtils.readData(path, Sheet.title, r, 12)
                    if Constants.customer == TestCaseId:
                        TestCustomer1(self.driver).TCP_AUT_GUI_RES_CUS_000_000_001_00001_POS_Test()

                    elif Constants.provider == TestCaseId:
                        TestProvider1(self.driver).TCP_AUT_GUI_RES_PRV_000_000_001_00002_POS_Test()

                    elif Constants.view == TestCaseId:
                        TestView1(self.driver).TCP_AUT_GUI_CFG_VWS_000_000_001_00004_POS_Test()

                    elif Constants.facility == TestCaseId:
                        TestFacility(self.driver).TCP_AUT_GUI_INV_MIV_L1L_LAYER1_001_00004_POS_Test()

                    elif Constants.circuit == TestCaseId:
                        TestCircuit(self.driver).TCP_AUT_GUI_INV_MIV_L1S_LAYER1_001_00005_POS_Test()

                    else:
                        print("test execution completed")
        finally:
            self.driver.close()
