# Python 3D Raycaster
A Raycaster made in Python and Pygame with minimal modules,

----

**Hey fellow developers!**

I've created a 'simple' 3d raycaster.  
So far it needs some more work, there's features that could be added, but mostly I just wanted to get the concept working.

So far, it seems a lot faster than otehr examples I've seen. :)

1.![screenShot1](screenShot1.PNG?raw=true "screenShot1")2. ![screenShot2](screenShot2.PNG?raw=true "screenShot2")

##Note
This only works for Python 3.*! (Could be converted)

##Features that could be added in the future:
* Textures.
* Sprites.
* HUD.

##Bugs:
* FishEye (groan).
* Rays seems to bend, not easily noticable.

##Problems
* My system for ray movement is very clunky. It uses steps, I may change this to use grid intersection.

#Installation
The installation is very easy, if you already have Python and Pygame installed.

----

* Run '`python main.py`' in cmd or for linux run `python3 main.py` (Not sure for Mac)

----

Otherwise if you don't have python and/or pygame, follow these steps: 
* Download python 3.* from: https://www.python.org/
* Run command '`pip install pygame‑1.9.2a0‑cp34‑none‑win_amd64.whl`' in cmd, same for linux (I think. Again not sure for Mac)

##In the Code
Let's go through some variables,  
```
w,h = [INT],[INT] (Screen resolution, Width and Height)
[...]
DEBUG = [BOOL] (Shows the Minimap,Rays and Player)
[...]
numRays = [INT] (Number of rays to shoot)
fov = [FLOAT] (Field Of View)

rayLength = [FLOAT] (How far each ray travels each step)
rayStep = [INT] (How many steps to take)
```

----

**Thank you** for reading this, I hope you find a use for this project.  
*Any help appreciated.*
