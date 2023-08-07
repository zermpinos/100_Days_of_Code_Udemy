from tkinter import *
import random
import timeit

# Create the GUI window
root = Tk()
root.title("Typing Speed Test")
root.geometry("990x540")

# Generate a list of words for the user to type
word_list = [
    "apple", "banana", "cherry", "date", "elderberry", "falcon", "giraffe", "honeycomb", "iguana", "jigsaw",
    "kangaroo", "leopard", "mountain", "narwhal", "octopus", "penguin", "quokka", "raccoon", "sapphire", "tiger",
    "umbrella", "violin", "waterfall", "xylophone", "yacht", "zebra", "amethyst", "butterfly", "cactus", "diamond",
    "elephant", "firework", "gazelle", "hedgehog", "island", "jackal", "kettle", "llama", "moccasin", "nightingale",
    "opulent", "paradox", "quagmire", "rhapsody", "serendipity", "talisman", "ubiquitous", "vivacious", "wanderlust",
    "xenophobia",
    "yonder", "zealous", "aplomb", "bewilder", "cacophony", "debonair", "effervescent", "facetious", "garrulous",
    "haphazard",
    "iconoclast", "juxtapose", "kaleidoscope", "labyrinth", "maelstrom", "nonchalant", "obfuscate", "panacea",
    "quintessential", "resilient",
    "sycophant", "transient", "ubiquity", "vexatious", "whimsical", "denial", "yesterday", "zeitgeist", "abstruse",
    "bucolic",
    "capricious", "delineate", "ephemeral", "flabbergast", "garrulity", "harbinger", "iconoclastic", "jejune", "kowtow",
    "luminous",
    "magnanimous", "nonplussed", "oblivion", "paradigm", "quizzical", "recalcitrant", "sycophantic", "taciturn",
    "ubiquitous", "vacillate",
    "wanton", "xenophobia", "yielding", "zealot", "amalgamate", "bombastic", "candor", "decorum", "egregious",
    "facetious",
    "gallivant", "hackneyed", "iconoclast", "juxtapose", "kaleidoscope", "labyrinth", "maelstrom", "nonchalant",
    "obfuscate", "panacea",
    "quintessential", "resilient", "sycophant", "transient", "ubiquity", "vexatious", "whimsical", "menial",
    "yesterday", "zeitgeist",
    "abstruse", "bucolic", "capricious", "delineate", "ephemeral", "flabbergast", "garrulity", "harbinger",
    "iconoclastic", "jejune",
    "kowtow", "luminous", "magnanimous", "nonplussed", "oblivion", "paradigm", "quizzical", "recalcitrant",
    "sycophantic", "taciturn",
    "ubiquitous", "vacillate", "wanton", "xenophobia", "yielding", "zealot", "alacrity", "bashful", "cacophony",
    "decadent",
    "ebullient", "fabricate", "garrulous", "hallowed", "iconoclast", "jubilant", "kinetic", "laconic", "maverick",
    "nonchalant",
    "obstinate", "paradox", "quaint", "rampant", "sacrosanct", "taciturn", "ubiquitous", "vexatious", "whimsical",
    "genial",
    "yielding", "zenith", "ambiguous", "benevolent", "candid", "diligent", "eloquent", "fabricate", "gallant",
    "hackneyed",
    "immutable", "judicious", "kinetic", "languid", "maverick", "nebulous", "obdurate", "pensive", "quixotic",
    "ravenous",
    "sagacious", "tenuous", "umbrage", "veracious", "wistful", "xenophobic", "yearn", "zealous"
]

random_words = " ".join(random.choices(word_list, k=10))

# Label to display the sample text
sample_label = Label(root, text=random_words)
sample_label.pack()

# Entry widget for user input
entry = Entry(root, width=30)
entry.pack()

# Variable to store the start time
start_time = 0


# Function to calculate typing speed
def calculate_speed():
    user_input = entry.get()
    words_typed = len(user_input.split())
    time_taken = timeit.default_timer() - start_time
    words_per_minute = words_typed / (time_taken / 60)
    print("Words per minute:", words_per_minute)


# Button to calculate typing speed
start_button = Button(root, text="End", command=calculate_speed)
start_button.pack()


# Start the timer when the user starts typing
def start_timer(_):
    global start_time
    if start_time == 0:
        start_time = timeit.default_timer()


entry.bind("<KeyPress>", start_timer)

# Run the GUI window
root.mainloop()
