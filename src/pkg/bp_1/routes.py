from pkg.bp_1 import bp




@bp.route('/')
def index():
   return 'bp_1/index'
