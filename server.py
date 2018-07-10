from flask import *
import praw
import os
import requests

user_agent="captainmeta4 api service on heroku"
app=Flask(__name__)
r=praw.Reddit(username="prawth_account",
              password=os.environ.get('rpassword'),
              client_id=os.environ.get('client_id'),
              client_secret=os.environ.get('client_secret'),
              user_agent=user_agent)

patreon_id=os.environ.get('patreon_id')
patreon_secret=os.environ.get('patreon_secret')
patreon_refresh=os.environ.get('patreon_refresh')
patreon_access=''

pledges={'1':[],
         '2':[],
         '3':[],
         '4':[],
         '5':[]}

@app.route('/')
def index():
    return "Successful GET"

@app.route('/patreonredirect')
def patreonredirect():
    code=request.args.get('code')
    
    #return code to patreon
    params={'client_id':patreon_id,
            'client_secret':patreon_secret,
            'redirect_uri':'http://api.captainmeta4.me/patreonredirect',
            'grant_type':'authorization_code',
            'code':code
           }
    headers={'User-Agent':user_agent,
             'Content-Type':'application/x-www-form-urlencoded'
            }
    x=requests.post('https://www.patreon.com/api/oauth2/token',params=params,headers=headers)
    data=x.json()
    
    #extract tokens
    access_token=data.get('access_token')
    refresh_token=data.get('refresh_token')
    
    #get user profile
    params={'access_token':access_token}        
    x=requests.get('https://www.patreon.com/api/oauth2/api/current_user',params=params,headers={'User-Agent':user_agent})
    
    #get user id
    user_id=x.json()['data']['id']
    
    
    
    params['includes']='pledges'
    #for testing purposes:
    
    return jsonify(y.json())
            
                          
def reload_pledges():
  
  params={'refresh_token':patreon_refresh,
          'grant_type':refresh_token}
          
  
  x=requests.post('http://www.patreon.com/api/oauth2/token',params=params, headers={'User-Agent':user_agent})
  x=x.json()
  patreon_access=x['access_token']
  
  #get pledges
  #x=requests.get('
  
  
  
@app.route('/auth', methods=["GET"])
def auth():
    #get key
    print(request.json)
    try:
        key=request.json.get('key')
    except AttributeError:
        print('no json')
        return jsonify({"valid":False, 'msg':'No key provided'})
    
    if key is None:
        return jsonify({"valid":False, 'msg':'No key provided'})

    #key is id. Fetch thing from reddit
    thing=next(r.info(fullnames=['t3_'+key]))

    if thing.subreddit.display_name != "prawthenticate":
        return jsonify({"valid":False, 'msg':'Invalid key provided'})
    elif not thing.is_self:
        return jsonify({"valid":False, 'msg':'Invalid key provided'})
    elif thing.selftext != "True":
        return jsonify({"valid":False, 'msg':thing.selftext})
    elif thing.selftext =="True":
        return jsonify({"valid":True, 'msg':"Approved"})
    

app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
