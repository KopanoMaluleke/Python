# #Week-4

**GUI Design Planning**

When it comes to planning your own GUI, keep it simple. Either sketch ideas on a piece of paper or play around with shapes on PowerPoint slides. There are probably better UX design tools out there, but these methods do the trick.

The goal of this GUI is to provide users with options to customize their digest email. They should be able to choose content sources, manage recipients, schedule sending time, and configure sender credentials. To start designing the GUI, instead of tackling the whole thing at once and feeling overwhelmed, break it down into smaller parts. 

The subsequent sections of the code follow a similar pattern to create different parts of the GUI. For instance, to add and remove recipients, a TKinter frame named "recipients frame" is created and inserted into the window. TKinter variables are instantiated to store recipient data, and these variables, along with the frame reference, are passed to the "build GUI recipients" function that handles creating the GUI widgets. The remaining sections of code follow a similar process to build other GUI sections, such as scheduling delivery time, configuring email content, updating sender credentials, and controlling settings updates.
