class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self):
        self.text = "This reply has been deleted."
        self.is_deleted = True

    def display(self, indent=0):
        if not self.is_deleted:
            print("    " * indent + f"{self.author}: {self.text}")
            for reply in self.replies:
                reply.display(indent + 1)

# Test
root_comment = Comment("It's a great book!", "Bob")
reply1 = Comment("The book is awful  :(", "Andrew")
reply2 = Comment("What was interesting in this book?", "Alice")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("You can kick it out...", "John")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()
