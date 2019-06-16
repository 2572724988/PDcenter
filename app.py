
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from config import COMMONINFO,NAVACTIVE,DB_URI
app = Flask(__name__)

@app.route('/<code>')
def navicate(code):
    NAVACTIVE.clear()
    COMMONINFO.pop('navmenu')
    NAVACTIVE[code] = 'active'
    COMMONINFO['navmenu'] = findparentlist(code)
    htmlfile = '%s.html'%(str(code))
    return render_template(htmlfile, commoninfo = COMMONINFO)

@app.route('/')
def Home():
    COMMONINFO.pop('navmenu')
    tsysmenus = SysMenu.query.all()

    COMMONINFO['menuinfo'] = tsysmenus
    COMMONINFO['navmenu'] = findparentlist('index')
    htmlfile = '%s.html'%(str('index'))
    return render_template(htmlfile, commoninfo = COMMONINFO)

# @app.route('/index')
# def index():
#     NAVACTIVE.clear()
#     NAVACTIVE['index'] = 'active'
#     return render_template('index.html', commoninfo = COMMONINFO)
#
# @app.route('/dashboard-social')
# def dashboard_social():
#     NAVACTIVE.clear()
#     NAVACTIVE['dashboard_social'] = 'active'
#     return render_template('dashboard-social.html', commoninfo = COMMONINFO)
#
# @app.route('/layouts')
# def layouts():
#     NAVACTIVE.clear()
#     NAVACTIVE['layouts'] = 'active'
#     return render_template('layouts.html', commoninfo = COMMONINFO)
#
# @app.route('/skins')
# def skins():
#     NAVACTIVE.clear()
#     NAVACTIVE['skins'] = 'active'
#     return render_template('skins.html', commoninfo = COMMONINFO)
#
# @app.route('/applayout')
# def applayout():
#     NAVACTIVE.clear()
#     NAVACTIVE['applayout'] = 'active'
#     return render_template('applayout.html', commoninfo = COMMONINFO)
#
# @app.route('/inbox')
# def inbox():
#     NAVACTIVE.clear()
#     NAVACTIVE['inbox'] = 'active'
#     return render_template('inbox.html', commoninfo = COMMONINFO)
#
# @app.route('/flot')
# def flot():
#     NAVACTIVE.clear()
#     NAVACTIVE['flot'] = 'active'
#     return render_template('flot.html', commoninfo = COMMONINFO)
#
# @app.route('/morris')
# def morris():
#     NAVACTIVE.clear()
#     NAVACTIVE['morris'] = 'active'
#     return render_template('morris.html', commoninfo = COMMONINFO)
#
# @app.route('/sparkline-charts')
# def sparkline_charts():
#     NAVACTIVE.clear()
#     NAVACTIVE['sparkline_charts'] = 'active'
#     return render_template('sparkline-charts.html', commoninfo = COMMONINFO)
#
# @app.route('/easypie-charts')
# def easypie_charts():
#     NAVACTIVE.clear()
#     NAVACTIVE['easypie_charts'] = 'active'
#     return render_template('easypie-charts.html', commoninfo = COMMONINFO)
#
# @app.route('/dygraphs')
# def dygraphs():
#     NAVACTIVE.clear()
#     NAVACTIVE['dygraphs'] = 'active'
#     return render_template('dygraphs.html', commoninfo = COMMONINFO)
#
# @app.route('/chartjs')
# def chartjs():
#     NAVACTIVE.clear()
#     NAVACTIVE['chartjs'] = 'active'
#     return render_template('chartjs.html', commoninfo = COMMONINFO)
#
# @app.route('/hchartable')
# def hchartable():
#     NAVACTIVE.clear()
#     NAVACTIVE['hchartable'] = 'active'
#     return render_template('hchartable.html', commoninfo = COMMONINFO)
#
# @app.route('/table')
# def table():
#     NAVACTIVE.clear()
#     NAVACTIVE['table'] = 'active'
#     return render_template('table.html', commoninfo = COMMONINFO)
#
# @app.route('/datatables')
# def datatables():
#     NAVACTIVE.clear()
#     NAVACTIVE['datatables'] = 'active'
#     return render_template('datatables.html', commoninfo = COMMONINFO)
#
# @app.route('/jqgrid')
# def jqgrid():
#     NAVACTIVE.clear()
#     NAVACTIVE['jqgrid'] = 'active'
#     return render_template('jqgrid.html', commoninfo = COMMONINFO)
#
# @app.route('/form-elements')
# def form_elements():
#     NAVACTIVE.clear()
#     NAVACTIVE['form_elements'] = 'active'
#     return render_template('form-elements.html', commoninfo = COMMONINFO)
#
# @app.route('/form-templates')
# def form_templates():
#     NAVACTIVE.clear()
#     NAVACTIVE['form_templates'] = 'active'
#     return render_template('form-templates.html', commoninfo = COMMONINFO)
#
# @app.route('/validation')
# def validation():
#     NAVACTIVE.clear()
#     NAVACTIVE['validation'] = 'active'
#     return render_template('validation.html', commoninfo = COMMONINFO)
#
# @app.route('/bootstrap-forms')
# def bootstrap_forms():
#     NAVACTIVE.clear()
#     NAVACTIVE['bootstrap_forms'] = 'active'
#     return render_template('bootstrap-forms.html', commoninfo = COMMONINFO)
#
# @app.route('/bootstrap-validator')
# def bootstrap_validator():
#     NAVACTIVE.clear()
#     NAVACTIVE['bootstrap_validator'] = 'active'
#     return render_template('bootstrap-validator.html', commoninfo = COMMONINFO)
#
# @app.route('/plugins')
# def plugins():
#     NAVACTIVE.clear()
#     NAVACTIVE['plugins'] = 'active'
#     return render_template('plugins.html', commoninfo = COMMONINFO)
#
# @app.route('/wizard')
# def wizard():
#     NAVACTIVE.clear()
#     NAVACTIVE['wizard'] = 'active'
#     return render_template('wizard.html', commoninfo = COMMONINFO)
#
# @app.route('/other-editors')
# def other_editors():
#     NAVACTIVE.clear()
#     NAVACTIVE['other_editors'] = 'active'
#     return render_template('other-editors.html', commoninfo = COMMONINFO)
#
# @app.route('/dropzone')
# def dropzone():
#     NAVACTIVE.clear()
#     NAVACTIVE['dropzone'] = 'active'
#     return render_template('dropzone.html', commoninfo = COMMONINFO)
#
# @app.route('/image-editor')
# def image_editor():
#     NAVACTIVE.clear()
#     NAVACTIVE['image_editor'] = 'active'
#     return render_template('image-editor.html', commoninfo = COMMONINFO)
#
# @app.route('/ckeditor')
# def ckeditor():
#     NAVACTIVE.clear()
#     NAVACTIVE['ckeditor'] = 'active'
#     return render_template('ckeditor.html', commoninfo = COMMONINFO)
#
# @app.route('/general-elements')
# def general_elements():
#     NAVACTIVE.clear()
#     NAVACTIVE['general_elements'] = 'active'
#     return render_template('general-elements.html', commoninfo = COMMONINFO)
#
# @app.route('/buttons')
# def buttons():
#     NAVACTIVE.clear()
#     NAVACTIVE['buttons'] = 'active'
#     return render_template('buttons.html', commoninfo = COMMONINFO)
#
# @app.route('/fa')
# def fa():
#     NAVACTIVE.clear()
#     NAVACTIVE['fa'] = 'active'
#     return render_template('fa.html', commoninfo = COMMONINFO)
#
# @app.route('/glyph')
# def glyph():
#     NAVACTIVE.clear()
#     NAVACTIVE['glyph'] = 'active'
#     return render_template('glyph.html', commoninfo = COMMONINFO)
#
# @app.route('/flags')
# def flags():
#     NAVACTIVE.clear()
#     NAVACTIVE['flags'] = 'active'
#     return render_template('flags.html', commoninfo = COMMONINFO)
#
# @app.route('/grid')
# def grid():
#     NAVACTIVE.clear()
#     NAVACTIVE['grid'] = 'active'
#     return render_template('grid.html', commoninfo = COMMONINFO)
#
# @app.route('/treeview')
# def treeview():
#     NAVACTIVE.clear()
#     NAVACTIVE['treeview'] = 'active'
#     return render_template('treeview.html', commoninfo = COMMONINFO)
#
# @app.route('/nestable-list')
# def nestable_list():
#     NAVACTIVE.clear()
#     NAVACTIVE['nestable_list'] = 'active'
#     return render_template('nestable-list.html', commoninfo = COMMONINFO)
#
# @app.route('/jqui')
# def jqui():
#     NAVACTIVE.clear()
#     NAVACTIVE['jqui'] = 'active'
#     return render_template('jqui.html', commoninfo = COMMONINFO)
#
# @app.route('/typography')
# def typography():
#     NAVACTIVE.clear()
#     NAVACTIVE['typography'] = 'active'
#     return render_template('typography.html', commoninfo = COMMONINFO)
#
# @app.route('/widgets')
# def widgets():
#     NAVACTIVE.clear()
#     NAVACTIVE['widgets'] = 'active'
#     return render_template('widgets.html', commoninfo = COMMONINFO)
#
# @app.route('/calendar')
# def calendar():
#     NAVACTIVE.clear()
#     NAVACTIVE['calendar'] = 'active'
#     return render_template('calendar.html', commoninfo = COMMONINFO)
#
# @app.route('/gmap-xml')
# def gmap_xml():
#     NAVACTIVE.clear()
#     NAVACTIVE['gmap_xml'] = 'active'
#     return render_template('gmap-xml.html', commoninfo = COMMONINFO)
#
# @app.route('/projects')
# def projects():
#     NAVACTIVE.clear()
#     NAVACTIVE['projects'] = 'active'
#     return render_template('projects.html', commoninfo = COMMONINFO)
#
# @app.route('/blog')
# def blog():
#     NAVACTIVE.clear()
#     NAVACTIVE['blog'] = 'active'
#     return render_template('blog.html', commoninfo = COMMONINFO)
#
# @app.route('/gallery')
# def gallery():
#     NAVACTIVE.clear()
#     NAVACTIVE['gallery'] = 'active'
#     return render_template('gallery.html', commoninfo = COMMONINFO)
#
# @app.route('/forum')
# def forum():
#     NAVACTIVE.clear()
#     NAVACTIVE['forum'] = 'active'
#     return render_template('forum.html', commoninfo = COMMONINFO)
#
# @app.route('/forum-topic')
# def forum_topic():
#     NAVACTIVE.clear()
#     NAVACTIVE['forum_topic'] = 'active'
#     return render_template('forum-topic.html', commoninfo = COMMONINFO)
#
# @app.route('/forum-post')
# def forum_post():
#     NAVACTIVE.clear()
#     NAVACTIVE['forum_post'] = 'active'
#     return render_template('forum-post.html', commoninfo = COMMONINFO)
#
# @app.route('/profile')
# def profile():
#     NAVACTIVE.clear()
#     NAVACTIVE['profile'] = 'active'
#     return render_template('profile.html', commoninfo = COMMONINFO)
#
# @app.route('/timeline')
# def timeline():
#     NAVACTIVE.clear()
#     NAVACTIVE['timeline'] = 'active'
#     return render_template('timeline.html', commoninfo = COMMONINFO)
#
# @app.route('/search')
# def search():
#     NAVACTIVE.clear()
#     NAVACTIVE['search'] = 'active'
#     return render_template('search.html', commoninfo = COMMONINFO)
#
# @app.route('/products-view')
# def products_view():
#     NAVACTIVE.clear()
#     NAVACTIVE['products_view'] = 'active'
#     return render_template('products-view.html', commoninfo = COMMONINFO)
#
# @app.route('/products-detail')
# def products_detail():
#     NAVACTIVE.clear()
#     NAVACTIVE['products_detail'] = 'active'
#     return render_template('products-detail.html', commoninfo = COMMONINFO)
#
# @app.route('/pricing-table')
# def pricing_table():
#     NAVACTIVE.clear()
#     NAVACTIVE['pricing_table'] = 'active'
#     return render_template('pricing-table.html', commoninfo = COMMONINFO)
#
# @app.route('/invoice')
# def invoice():
#     NAVACTIVE.clear()
#     NAVACTIVE['invoice'] = 'active'
#     return render_template('invoice.html', commoninfo = COMMONINFO)
#
# @app.route('/login')
# def login():
#     NAVACTIVE.clear()
#     NAVACTIVE['login'] = 'active'
#     return render_template('login.html', commoninfo = COMMONINFO)
#
# @app.route('/register')
# def register():
#     NAVACTIVE.clear()
#     NAVACTIVE['register'] = 'active'
#     return render_template('register.html', commoninfo = COMMONINFO)
#
# @app.route('/forgotpassword')
# def forgotpassword():
#     NAVACTIVE.clear()
#     NAVACTIVE['forgotpassword'] = 'active'
#     return render_template('forgotpassword.html', commoninfo = COMMONINFO)
#
# @app.route('/lock')
# def lock():
#     NAVACTIVE.clear()
#     NAVACTIVE['lock'] = 'active'
#     return render_template('lock.html', commoninfo = COMMONINFO)
#
# @app.route('/error404')
# def error404():
#     NAVACTIVE.clear()
#     NAVACTIVE['error404'] = 'active'
#     return render_template('error404.html', commoninfo = COMMONINFO)
#
# @app.route('/error500')
# def error500():
#     NAVACTIVE.clear()
#     NAVACTIVE['error500'] = 'active'
#     return render_template('error500.html', commoninfo = COMMONINFO)
#
# @app.route('/blank')
# def blank():
#     NAVACTIVE.clear()
#     NAVACTIVE['blank_'] = 'active'
#     return render_template('blank_.html', commoninfo = COMMONINFO)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class UserModel(db.Model):
    __tablename__ = 'user_model'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)

    def __repr__(self):
        return "<User(username: %s)>" % self.username

class SysMenu(db.Model):
    __tablename__ = 't_sysmenu'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    code = db.Column(db.String(64),nullable=True)
    name = db.Column(db.String(128), nullable=False)
    navigate_url = db.Column(db.String(256), nullable=True)
    icon = db.Column(db.String(256), nullable=False)
    parent_id = db.Column(db.Integer, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    sequence = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Integer, nullable=False)

def findparentlist(code):
    navigateList = []
    result1 = SysMenu.query.filter(SysMenu.code == code).first()
    if result1.parent_id == 0:
        navigateList.append(result1)
        return navigateList
    else:
        navigateList.append(result1)
        while True:
            result2 = SysMenu.query.filter(SysMenu.id == result1.parent_id).first()
            navigateList.append(result2)
            result1 = result2
            if result1.parent_id == 0:
                break
        return reversed(navigateList)
# findparentlist('')
# for i in findparentlist('QpmsPro'):
#     print(i.id)
# db.drop_all()
# db.create_all()
# tsysmenus = SysMenu.query.all()
# for i in tsysmenus:
#     print(i.name)117.136.40.230
if __name__ == '__main__':
    app.run(host='127.0.0.1',port= 5000,debug=True)
