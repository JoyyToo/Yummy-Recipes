import os
from app.views import app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run('', port=port)
