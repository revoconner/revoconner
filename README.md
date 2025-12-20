<div align="center">
<img src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Frevoconner&label=Hello%20visitor%20number&labelColor=%23333333&countColor=%23362663" height="auto" width="430"><br><br><br>
<div align="left">
<b>
Tech artist from the Himalayas. Is it beautiful you ask, of course it is, but more than that its great for overclocking!

I am a tech artist , self taught (is that what people who couldn't manage college say?), by profession. 

How have I ever built anything for Blender without being able to turn the viewport around properly! But then again looking back at how I even began to write code, it's a miracle in itself. Oh! You wanna hear that story? Well, I used to be a character artist for half a decade (I still am... in parts), became a senior character artist and then my employers at the time decided I was expendable and should become a tech artist in a few months along with my regular duties with no extra pay!! Yaay!!

But at least it got me into this, and it's good work, so, ummm a win in the end?

Ex-mountaineer, looking back now I should have used rope while climbing in the Himalayas, probably wouldn't have been "ex" then. I like to drive sometimes and then call myself a petrolhead, how does a carburetor work again??
</b></b></b>
<h2>Some of the work I am proud of doing as a tech artist include: </h2>


<details>
<summary><h3>Listed here as a summary of each work, expand to read.</h3></summary>

<ul align="left">
<details>
<summary><h4>The first public metahuman transfer tool for Maya.</h4></summary>

It's deprecated now since it was a very early prototype before much of the documentations, that are available today, were available.
</details>
</ul>

<ul align="left">
<details>
<summary><h4>Modifying Meta SDK for Quest 3 in Unity to overcome the hardware limitation of depth sensor.</h4></summary>

Typically if you build a mixed reality game, you can only see objects up to about 8 meters. I modified some SDK files to get unlimited range with working occlusion through clever masking tricks. I was also able to solve the issue of occlusion glitching out if there is glass windows around the area by adding another mask to the depth texture. Running a RenderDoc profile for the build I was also able to optimise the SDK further saving a tiny bit of performance after the changes.
</details>
</ul>

<ul align="left">
<details>
<summary><h4>The first publicly available Vertex ID transfer tool for 3ds Max.</h4></summary>

It's not the most performant tool but it works.
</details>
</ul>

<ul align="left">
<details>
<summary><h4>Created a shapekey (blendshape) for Blender that works based on UVs.</h4></summary>

So it's a shapekey that works irrespective of topological differences.
</details>
</ul>

<ul align="left">
<details>
<summary><h4>Bulk redirector fixup tool for UE 4.27 to save myself from editor crashes.</h4></summary>

I cannot imagine why there is no safeguard for this when renaming or moving assets in bulk. I am not so sure it will work in UE5.
</details>
</ul>

<ul align="left">
<details>
<summary><h4>Unity - Build time texture atlasing for VR (early alpha).</h4></summary>

No UV remapping in shader, no manual material changes, nothing destructive. How it works is it scans world positions of all the props in a scene and predefined .meta file of textures to get the texel density.
</details>
</ul>

<ul align="left">
<details>
<summary><h4>Software based VT (streamable in chunks) for multi asset streaming on mobile VR for Unity.</h4></summary>

Most of the implementation of SVT in unity (and there aren't a lot, especially none I could find for mobile), are for terrains or very large meshes. For a mixed reality build it doesn't really work. That means you cannot really cut down on sampler calls, because large atlases will hit memory limits. I transferred most of the calculations of streaming data from CPU to GPU, saving that CPU bound performance impact it could have had on a VR headset. It streams the texture in chunks together with the right mip levels, saving huge amount of memory cost that would have been taken with large atlases. This in turn with the previous solution means fewer sampler calls, and non destructive atlases that can be streamed without resolution or size limits for memory.
</details>
</ul>

<ul align="left">
<details>
<summary><h4>Unity - Mesh to primitive collider converter, first editor tool for this as far as I know.</h4></summary>

Converts imported mesh (marked as colliders) from DCC app like Maya or blender to Unity's primitive box collider instead of the default mesh collider it would have been. Primitive colliders are more performant than mesh colliders but making them in Unity's editor is really a painful way to spend the time. This solves that issue.
</details>
</ul>

<ul align="left">
<details>
<summary><h4>Unity - A shader variant collection tool for editor.</h4></summary>

The usual method to collect shaders in Unity is to turn on logging, play and get the log to see what variants have been used. It's just not very efficient. The editor tool I created lets you do that with a user friendly UI (because let's be honest no one wants to use the inbuilt shader variant inspector), but more importantly automation for collecting runtime variants with a few clicks.
</details>
</ul>

<ul align="left">
<details>
<summary><h4>A realtime asset reference protector and replacement manager for Unity (early prototype).</h4></summary>

Just like the reference warning you get when you delete an asset in Unreal that might break something else. It's not an easy thing to do, especially when working with multiple git branches. Unity's GUID system instead of relying on relative path for reference is a terrible thing, the logic behind the tool uses a kernel level daemon (Windows only for now) to watch file changes and then fetch known patterns from those files to reference in a sqlite3 database.
</details>
</ul>

<ul align="left">
<details>
<summary><h4>Unity - Colliderless culling for particle system to save all those CPU calls that colliders make.</h4></summary>

At spawn uses matrices to check the world transform of objects inside a radius from the point of spawn. Then uses shader's alpha to cull the particle if it touches an object like walls, or floors etc.
</details>
</ul>

<div align="left">
<div id="user-content-toc">
  <ul align="left" style="list-style: none;">
    <summary>
      <h3>Non tech art related personal project:</h3>
    </summary>
  </ul>
</div>

<ul align="left">
<details>
<summary><h4>A truly invisible terminal emulator that runs entirely headless but returns isatty() true to spawned processes.</h4></summary>

Useful for running TUI apps that crash without tty support and do not support headless mode. (e.g. - Windows native Claude code in interactive mode). Is really truly headless, most headless terminal apps I have seen do spawn a console if run without no console flag, or directly from the executable binary. Bidirectional termination to prevent orphaned processes. Supports any CLI app, including any TUI apps, or GUI apps. Supports and keeps track of multiple child, grandchild, etc processes. Can be run from the system tray or truly headless. If you choose to run from the tray, it can be used to interact with an otherwise headless terminal CLI/TUI app whenever you want.
</details>
</ul>

<ul align="left">
<details>
<summary><h4>A truly local photos app for sorting photos by facial recognition.</h4></summary>

Great for everyday users to sort all their photos, hundreds of thousands of photos locally, without the need to spend money on online storage. It differs from competition in the fact that it's really easy to use with a focus on everyday users, install it, point to the folder where your photos are, and just let it do its thing. It's accurate, even for blurry faces or side faces, without the need to micro manage such as manual tagging to get better results. I wanted to keep the UI simple instead of packing in pro features, there are already photo managers out there for professionals, not one accurate facial recognition and organiser for someone who doesn't want to deal with a complex UI.

- 99.9% accuracy at 40% threshold, including covered, blurry, or side faces as well as low light scenarios.
- Path exclusion/inclusion with explorer or wildcards, hiding people or specific photos of someone, changing thumbnails
- Auto rename conflict resolution
- Sorting by count or name
- Hiding unknown people
- Filtering people from the background by toggling on a button
- Jumping to names
- Dynamic auto-scan with four modes
- Recalibration does not require rescan
- Thumbnail size controllable with a slider
</details>
</ul>
</details>
</div>
</div>
<br>

---
<br><br><br>
<div align="center">
<h1>Say hello!</h1>
</div>
<br><br>
<a href="mailto:revoconner+j5jdc38r@live.com"><img src="https://github.com/revoconner/revoconner/raw/refs/heads/main/images/social_alt/email.svg" height="50" width="auto"></a>
<img src="https://github.com/revoconner/revoconner/raw/refs/heads/images/combined/separator.svg" height="auto" width="2">
<a href="https://www.revoconner.com"><img src="https://github.com/revoconner/revoconner/raw/refs/heads/main/images/social_alt/website.svg" height="50" width="auto"></a>
<img src="https://github.com/revoconner/revoconner/raw/refs/heads/images/combined/separator.svg" height="auto" width="2">
<a href="https://www.artstation.com/revoconner"><img src="https://github.com/revoconner/revoconner/raw/refs/heads/main/images/social_alt/artstation.svg" height="50" width="auto"></a>
<img src="https://github.com/revoconner/revoconner/raw/refs/heads/images/combined/separator.svg" height="auto" width="2">
<a href="https://www.youtube.com/@revoconner"><img src="https://github.com/revoconner/revoconner/raw/refs/heads/main/images/social_alt/youtube.svg" height="50" width="auto"></a>
<img src="https://github.com/revoconner/revoconner/raw/refs/heads/images/combined/separator.svg" height="auto" width="2">
<a href="https://www.linkedin.com/in/revoconner"><img src="https://github.com/revoconner/revoconner/raw/refs/heads/main/images/social_alt/linkedin.svg" height="50" width="auto"></a>
<br><br><br>
</div>
<br>


<div align="center">
<img src ="https://github.com/revoconner/revoconner/raw/refs/heads/main/images/combined/programming_dark.svg" height="auto" width="40%"><img src="https://github.com/revoconner/revoconner/raw/refs/heads/images/combined/separator.svg" height="auto" width="10%"><img src ="https://github.com/revoconner/revoconner/raw/refs/heads/main/images/combined/techart_dark.svg" height="auto" width="40%">
</div>

---

<div align="center">
<div id="user-content-toc">
  <ul align="center" style="list-style: none;">
    <summary>
      <h1>Some standalone scripts</h1>
    </summary>
  </ul>
</div>
<br>
<a href="https://gist.github.com/revoconner/0df178ba073a54c3600a95c80f191258"><img height="auto" width="400" src="https://github.com/revoconner/revoconner/raw/refs/heads/main/images/gists/uv_layout_othershell_aware.svg"></a>
<a href="https://gist.github.com/revoconner/fd0c6da4c7bfd2de8ecd32a5ae485b46"><img height="auto" width="400" src="https://github.com/revoconner/revoconner/raw/refs/heads/main/images/gists/fbx-colliders-card.svg"></a>
<a href="https://gist.github.com/revoconner/b21bae3e6b824e2ed61d257bbfff8519"><img height="auto" width="400" src="https://github.com/revoconner/revoconner/raw/refs/heads/main/images/gists/reddit-tampermonkey.svg"></a>
</a><a href="https://gist.github.com/revoconner/fe38d31ff756b167a7d27742f5eaa030"><img height="auto" width="400" src="https://github.com/revoconner/revoconner/raw/refs/heads/main/images/gists/align-pivot-card.svg"></a>
<br><br><br>
</div>

---

<div align="center">
<div id="user-content-toc">
  <ul align="center" style="list-style: none;">
    <summary>
      <h1>Computer go brrrrr!</h1>
    </summary>
  </ul>
</div>
  <br>
<img src="https://img.shields.io/badge/C%23-239120?style=for-the-badge&logo=unity&logoColor=white" height="28" width="auto">&nbsp;&nbsp;&nbsp;&nbsp; 
<img src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" height="28" width="auto">&nbsp;&nbsp;&nbsp;&nbsp; 
<img src="https://img.shields.io/badge/bat-4D4D4D?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBkPSJNNCA2bDYgNi02IDYiLz48cGF0aCBkPSJNMTIgMThoOCIvPjwvc3ZnPg==&logoColor=white" height="28" width="auto">&nbsp;&nbsp;&nbsp;&nbsp; 
<img src="https://img.shields.io/badge/py-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" height="28" width="auto">&nbsp;&nbsp;&nbsp;&nbsp; 
<img src="https://img.shields.io/badge/JS-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" height="28" width="auto">&nbsp;&nbsp;&nbsp;&nbsp; 
<img src="https://img.shields.io/badge/Pwsh-5391FE?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0yLjE1IDdsNy4yNiA1LjMzLTcuMjYgNS4zNCAyLjA3IDIuODMgMTAuMjktNy41Ni4wMS0xLjIyTDQuMjIgNC4xN3ptMTAuNTQgMTEuMzJ2Mi41Mmg5LjE2di0yLjUyeiIvPjwvc3ZnPg==" height="28" width="auto">&nbsp;&nbsp;&nbsp;&nbsp; 
<img src="https://img.shields.io/badge/Ahk-334455?style=for-the-badge&logo=autohotkey&logoColor=white" height="28" width="auto">&nbsp;&nbsp;&nbsp;&nbsp; 
<img src="https://img.shields.io/badge/Asm-525252?style=for-the-badge&logo=assemblyscript&logoColor=white" height="28" width="auto"><br>
<br><br><br>
</div>


