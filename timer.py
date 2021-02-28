``` Python
from kivy.app import App
from kivy.clock import Clock

#Main Base,this is there only for reference
GridLayout:
  cols: 1
  Label:
    id:counter
    text: "0"
  TextInput:
    id: input
   



class MainApp(App):
  #Makes the timer add one number per second until it reaches 600 seconds(10 minutes)
  def on_start(self):
    self.function_interval = Clock.scheduele_interval(self.update_label, 1)
    Clock.scheduele_once(self.focus_text_input, 1)#THIS line of code is not necessarily needed but we could keep it there if we want to
    Clock.scheduele_once(self.stop_interval, 600) 
    
 
 #This function is there to stop the clock when a specific number has been reached
 def stop(self, *args):
  self.function_interval.cancel()
 
 
 #This function is there to focus on the screen only when the timer starts
  def focus_text_input(self, *args):#THIS function is not necessarily needed
    self.root.ids.input.focused = True
  
  
  
  #This function is there to add the number 1 to the timer after one second.
  def update_label(self, *args):
    #Update the label  
    mine.root.ids.counter.text = str(int(mine.root.ids.counter.text) + 1)




MainApp().run()it 

```
