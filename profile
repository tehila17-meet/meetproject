fav = session.query(Favs).filter_by(user = user_id).first()
		dive = session.query(Places).filter_by(id = fav.place).first()
		
		
		
		
		#user = session.query(User).filter_by(name = login_session['fullname']).first()
		user = session.query(User).filter_by(id = user_id).first()
		user1 =  session.query(User).filter_by(name= login_session['fullname']).first()
		
		#new_favorite = Favs(place = place_id,user = user.id)
		return render_template('profile.html',user=user,fav=fav,dive=dive,user1 = user1)