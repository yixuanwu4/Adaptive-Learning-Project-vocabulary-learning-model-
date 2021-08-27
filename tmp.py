# import inquirer


# # This step asks the user to pick the level of words to practice
# questions = [
#   inquirer.List('size',
#                 message="Hi, which level of vocabulary do you wish to practice ?",
#                 choices=['CET4', 'CET6', 'TOEFL'],
#             ),
# ]
# answers = inquirer.prompt(questions)
# # print(answers["size"])

import tkinter as tk

def reveal(event):
    label = event.widget
    label.configure(text=label.full_text)

root = tk.Tk()
root.geometry("4000x1000")
word_frame = tk.Frame(root, borderwidth=1, relief="sunken")
word_frame.pack(side="top", fill="x", padx=20, pady=20)

term = "Just back from a tour of several Arabian Gulf1 countries, a woman recalls how jumpy she felt talking to men there. “Not because of what they said, ”she explains,“ but what they did with their eyes. ”Instead of the occasional blink, Arabs lowered their lids so slowly and languorously that she was convinced they were falling asleep. In Japan eye contact is a key to the way you feel about someone. And the less of it,the better. What a Westerner considers an honest look in the eye , the Oriental takes as a lack of respect and a personal affront. Even when shaking hands or bowing — and especially when conversing6 — only an occasional glance into the other person’s face is considered polite. The rest of the time , great attention should be paid to fingertips, desktops,and the warp and woof of the carpet.“Always keep your shoes shined in Tokyo, ”advises an electronics representative who has spent several days there .“You can bet a lot of Japanese you meet will have their eyeson them. ”"
for word in term.split():
    letter = word
    label = tk.Label(word_frame, text=letter, borderwidth=1, 
                     font=("Helvetica", 18))
    label.full_text = word
    label.pack(side="left")
    label.bind("<1>", reveal)

tk.mainloop()