class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.name = ''
        self.post = ''
        self.loggdin = False
        self.menu()
    
    def menu(self):
        user_input = input('''Welcome to chatbook , please follow the instructions
        1. sign up
        2. sign in
        3. write a post
        4. delete the post
        5. exit\n''')
        if user_input=='1':
            self.sign_up()
        if user_input=='2':
            self.sign_in()
        if user_input=='3':
            if self.loggdin ==True:
                self.write_post()
            else:
                print('Please sign in to write a post')
        if user_input=='4':
            if self.loggdin ==True:
                self.delete_post()
            else:
                print('Please sign in to delete a post')
        if user_input=='5':
            exit()

    def sign_up(self):
        email = input('enter your email id here - ')
        password = input('enter your password here - ')
        name = input('enter your name here - ')
        self.username = email
        self.password = password
        self.name = name
        print('sign up sucesssfully')
        self.menu()

    def sign_in(self):
        if self.username=='' or self.password=='':
            print('Please sign up first')
        else:
            email = input('Enter your email id here - ')
            password = input('Enter your password here - ')
            if email ==self.username and password==self.password:
                print(f'Welcome back {self.name}')
                self.loggdin = True
                if self.post =='':
                    print('You havent posted in a while - create one here')
                    yes_no = input('''Y - want to write a post
                    N - dont want to write a post\n''')
                    if yes_no =='Y':
                        self.write_post()
                    
                else:
                    print(f'''{self.name}, you have written
                    {self.post}''')
                    print('do you want to delete your previous post?')
                    yes_no = input('''Y - want to post
                    N - dont want to delete a post\n''')
                    if yes_no=='Y':
                        self.delete_post()
                self.menu()
            else:
                print('Kindly enter correct credentials')
        self.menu()       
    
    def write_post(self):
        self.post = input('Enter your post below\n')
    
    def delete_post(self):
        self.post = ''
        print('Previous post has been deleted')

obj = chatbook()

