from moonmask import collage

c = collage.Collage()
c.set_moon_mask(date="2019-02-01")
#c.set_moon_foreground(instagram_url="https://www.instagram.com/p/Bs9mVqinOWQ/")
c.set_main_image(instagram_url="https://www.instagram.com/p/BuMPF3qgWAt/")
#c.set_main_background(instagram_url="https://www.instagram.com/p/BkcL_Gdnch7/")
c.make_collage("todays_moon")
