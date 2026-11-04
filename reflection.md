## COMPONENTS

# Tkinter Form
TkInter is the toolkit that draws the window, the form, and the entry field visuals for the user

# Validation
These are the error checks created for each field with validation tests appropriate for each to help ensure data validity based on format, acceptable range, etc.

# JSON
this step converts the entry values into a JSON text string 

# POST
this is the section of code that sends the data to the server, the HTTP verb  action

# Flask API
Receives the post, verifies the name was supplied prints the data to its console, and sends a reply back like status:ok


## STEPS
I followed my normal process, where I copied the provided example exactly. Then I ran the test, and I entered the form elements with acceptable values. Then I tried adding some wrong values to see how it would respond.

Then I went back and I started making the changes by adding in the new fields and removing the other fields. What I do is, usually, I do it like an assembly line: I copy the name, then I repaste it three times, and then I edit it.

Now, the one thing that I did so that I had more control over verifying that they entered a valid numeric amount for price was to make price a string. That way, I can test to ensure that if they didn't enter a number, I could catch that. It would accept it, but then I could give an error saying, "This isn't a valid number." That way, I have more control over the error messaging, which is why I did price as a string.

In this case, I went ahead and I added the different values for the variables for the test, for the form, and then for the collect data to the dictionary. Then I went ahead and did the testing. dddd

## SURPRISE

This one didn't surprise me so much because it felt very methodical. I think the main thing that surprised me was the following: how it was defined. I would say the biggest thing was actually thinking about how the data is appended together or concatenated together into the dictionary value, which makes sense because I've seen how it passes it. I'm not used to seeing individual variables and their values concatenated together, so that was a little of a surprise, and just seeing how the different pieces come together for it to work 

## UNDERSTAND

I think I understand a little bit better about how this process works, but now I'm wondering: is this the general structure, or is there more complexity to this, or is it basically how this is? This is really most of it. This was a straightforward form. Are there ways they get customized? I'm sure they do, but I guess it's just: what are the next steps? It's not embedded enough to feel intuitive yet, so I would like it to feel that way if this is something we'll be working with more. 


