from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MarginCalck(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols=1
        self.window.size_hint={0.7, 0.8}
        self.window.pos_hint={"center_x": 0.5, "center_y":0.5}

        self.InPriceText=Label(text='IN')
        self.window.add_widget(self.InPriceText)
        self.InPrice=TextInput(text='3.0', multiline=False, halign='center', input_filter='float')
        self.window.add_widget(self.InPrice)

        self.TPText=Label(text='TP')
        self.window.add_widget(self.TPText)
        self.TP=TextInput(text='5.0', multiline=False, halign='center', input_filter='float')
        self.window.add_widget(self.TP)

        self.SLText=Label(text='SL')
        self.window.add_widget(self.SLText)
        self.SL=TextInput(text='2.5', multiline=False, halign='center', input_filter='float')
        self.window.add_widget(self.SL)

        self.RiskText=Label(text='Risk $')
        self.window.add_widget(self.RiskText)
        self.Risk=TextInput(text='10', multiline=False, halign='center', input_filter='int')
        self.window.add_widget(self.Risk)


        self.CalculateResult1=Label(text='', bold=True, font_size=24)
        self.window.add_widget(self.CalculateResult1)
        self.CalculateResult2=Label(text='')
        self.window.add_widget(self.CalculateResult2)
        #add widgets to window
        self.button=Button(text='Calculate', bold=True)
        self.button.bind(on_press=self.CalculatePosition)
        self.window.add_widget(self.button)

        return self.window

    def CalculatePosition(self, instance):
        self.nInPrice = float(self.InPrice.text)
        self.nTakePrice = float(self.TP.text)
        self.nStopPrice = float(self.SL.text)
        self.nRiskValue = int(self.Risk.text)

        if (self.nInPrice != 0) and (self.nStopPrice != self.nInPrice) :
            if self.nStopPrice > self.nInPrice:
                self.nPercent = round((self.nStopPrice * 100 / self.nInPrice) - 100, 2)
                self.nRatio = round((self.nInPrice - self.nTakePrice) / (self.nStopPrice - self.nInPrice), 1)
                self.CalculateResult1.color='red'
            #            LabelOrderVolume["fg"] = 'red'
            else:
                self.nPercent = round(100 - (self.nStopPrice * 100 / self.nInPrice), 2)
                self.nRatio = round((self.nTakePrice - self.nInPrice) / (self.nInPrice - self.nStopPrice), 1)
                self.CalculateResult1.color='green'
#            LabelOrderVolume["fg"] = 'green'

#        print(f"Вход={self.nInPrice} Тейк={self.nTakePrice} Стоп={self.nStopPrice} Риск={self.nRiskValue}")

            self.nValue = int((self.nRiskValue * 100) / self.nPercent)
            self.nPos = self.nValue / self.nInPrice

            if self.nPos>=1:
                self.nPos = round(self.nPos, 0)
            else:
                self.nPos = round(self.nPos, 4)

            self.nLeverage = int(100 / self.nPercent)

            self.CalculateResult1.text=" " + self.InPrice.text+" "+\
                                       self.TP.text+" "+\
                                       self.SL.text+" "+\
                                       self.Risk.text
            self.CalculateResult1.text =f"Coins={self.nPos}    Max Leverage={self.nLeverage}x"
            self.CalculateResult2.text = f"${self.nValue}  {self.nPercent}%  Sl/Tp=1/{self.nRatio}"
        else:
            self.CalculateResult1.color = 'red'
            self.CalculateResult1.text =f"!!!!!!! ERROR !!!!!!!!"
            self.CalculateResult2.text = ""

if __name__ == "__main__":
    MarginCalck().run()