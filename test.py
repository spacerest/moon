#from moonmask.moonmask_ui import MoonMaskUI

#ui = MoonMaskUI()

#ui.show_info()
#ui.show_tutorial()
#c = collage.Collage()
#c.set_moon_mask(relative_date="today")#date="2019-02-01")
#c.set_moon_foreground(instagram_url="https://www.instagram.com/p/Bs9mVqinOWQ/")
#c.set_main_image(instagram_url="https://www.instagram.com/p/BuMPF3qgWAt/")
#c.set_main_background(instagram_url="https://www.instagram.com/p/BkcL_Gdnch7/")
#c.make_collage("todays_moon")

from moonmask.collage import Collage

c = Collage()

c.set_mask()

c.set_main_image("parachute", url="https://lh3.googleusercontent.com/lZxrIsm3j_6pyXhWnXzv31UkCAVxO3oRRSRkQJksJkTrQ4e-OC9jdhelQSDlswSEdnjOUzcz6KGMT4trcpZgENwmwPM31OP4Lcoo-XFcH4MFuAOQHdyx4EXNAAzoydTpSOoaRFRUVYvGtMXaMeyjkItvJMUyiDDnovK-n2Y-x69YPHklpnxcp75ljoNGr8wtj5oh3JFv2oiYRPgszcmlzme1i6MT0pKPj6980NqdSyr469MRKD1297FL1fTnjkpBspxdQeXBfJOAfGdcrstv5WSUUeQ4yo77ORrULwkpK_a1uPG7d_As6wfNeDP0rbsNxVQXHGJDxM1nOFbluA8nT3kFCOQ5hRqRB-FwNmslqX9KrxdbB7ekbeuiY5PhVwLFWuaJnPKM-s-WdlWLlBGPi8kjJ5qKT30ZhunEGtxRZC7L4A-bT1onwB4vU_H5fRqmP6GetQledLb_-GqXiV7PdzeWrRYiAis23rgdzdmipIJCttZmu1pH6fBiEzXaYzlPsxYB2UU34wqmqOs3C-5iHyr71nAOA7_pHSWOa6nrKpu7gZFMhJY3EM6WfaVwMnGxL6bkPdYheQUeOasb-GqvA7ZZt7JxR8UGh0SC7rxCUYGOKuQ5w8_folxxgppv2RT-4Sm8KOL6Ay4GZz-TL_7dIPbaImj8-omI=w846-h634-no")#instagram_url="https://www.instagram.com/p/BnfsUS9ngZI/")
c.set_mask_negative_space("black", color="black")
c.set_mask_positive_space("white", color="white")
c.pixelate_negative_space()

#c.set_positive_space_words(words="test")
#c.set_negative_space_words(words="*", invert=True)
c.create_collage("hi3", negative_space_transparency=150, dimensionality=7)
c.save_collage("h13")
