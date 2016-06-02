from system.core.controller import *
class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('Model')
    def index(self):
        return self.load_view('main.html')
    def main(self):
        pokes = self.models['Model'].poked_me(session['id'])
        infos = self.models['Model'].show_poked()
        total_poked = self.models['Model'].total_poked(session['id'])
        return self.load_view('userpage.html', pokes = pokes, infos=infos, total_poked = total_poked)
    def addpoke(self, user_id, poster_id):
        pokes = self.models['Model'].poke_user(user_id, poster_id)
        return redirect ('/main')
    def register(self):
        user_info = self.models['Model'].register(request.form)
        if user_info['status'] == True:
            session['id'] = user_info['user']['id'] 
            session['name'] = user_info['user']['name']            
            return redirect('/main')
        else:
            for message in user_info['errors']:
                flash(message)
            return redirect('/')
    def login(self):
        login_info = self.models['Model'].login(request.form)
        if login_info['status'] == True:
            session['id'] = login_info['user']['id'] 
            session['name'] = login_info['user']['name']
            return redirect('/main')
        else:
            for message in login_info['errors']:
                flash(message)
            return redirect('/')
    def logoff(self):
        session.clear()
        return redirect('/')
