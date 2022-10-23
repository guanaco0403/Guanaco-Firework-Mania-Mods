![Icon Logo](https://avatars.githubusercontent.com/u/76651037?s=48&v=4)

---
Hello, This Guide will help you Starting Scripting Fireworks Mania mods in unity.<br/>
Please Keep in mind that scripting is not easy for beginers.<br/>
---
**Created by Guanaco0403**

Don't forget to join the [firework mania Discord Server](https://discord.gg/6TJPwUUrJp)

# Table of Contents

### • [First Scripting Setup](#First-Scripting-Setup)

### • [Starting Scripting](#Starting-Scripting)

### • [Unity Scripting Basics](#Unity-Scripting-Basics)

### • [Fireworks Mania Scripting Functions](#Fireworks-Mania-Scripting-Functions)

### • [Starting a Script at Mod Start](#Starting-a-Script-at-Mod-Start)

### • [Troubleshooting](#Troubleshooting)

### • [Bug Report, Question Or Suggestion](#Bug-Report-Question-Or-Suggestion)
<br/>

# First Scripting Setup:

## Step 1
To start, you must have followed all the steps in order to configure unity for fireworks mania modding.<br/>
You can find this guide by [clicking here](https://github.com/Laumania/FireworksMania.ModTools#getting-started).

**IMPORTANT, MAKE SURE YOU CLOSED UNITY BEFORE GOING TO NEXT STEP!!!**<br/>
After you have successfully completed each step to configure unity for modding, you can move on to **step 2**.

## Step 2
You now need to install and configure the software that will allow you to create scripts and will also allow unity to compile them so that they can be recognized by the game.

**First**, go to **Unity Hub** and click on **"Installs"** in the list on the left.

![](https://github.com/guanaco0403/Guanaco-Firework-Mania-Mods/blob/main/Images/Scripting-Guide/UnityHub1.png)

**Then**, Click on the⚙️icon of the unity version used for modding (currently 2021.3.9f1).

![](https://github.com/guanaco0403/Guanaco-Firework-Mania-Mods/blob/main/Images/Scripting-Guide/UnityHub2.png)

**Then**, click on **"Add modules"**.

![](https://github.com/guanaco0403/Guanaco-Firework-Mania-Mods/blob/main/Images/Scripting-Guide/UnityHub3.png)

**Then**, make sure that **"Microsoft Visual Studio Community 2019"** is installed, if not, select it and select **"Install"**.

![](https://github.com/guanaco0403/Guanaco-Firework-Mania-Mods/blob/main/Images/Scripting-Guide/UnityHub4.png)

**Once all of this is done**, you can start Unity and move on to the **next step**.

## Step 3
we will now configure **Visual Studio 2019** with **unity**.<br/>
to do this, **Start Unity** and go to **"Edit" ➞ "Preferences"**.

![](https://github.com/guanaco0403/Guanaco-Firework-Mania-Mods/blob/main/Images/Scripting-Guide/Unity1.png)

**Then**, select **"External Tools"**, and then select **"Microsoft Visual Studio 2019"** from the **"External Script Editor"** list.

![](https://github.com/guanaco0403/Guanaco-Firework-Mania-Mods/blob/main/Images/Scripting-Guide/Unity2.png)

You can then close the window as well as **unity** and **unity hub** and then reopen **unity hub** and then start **unity**.<br/>
**once unity has started**, please make sure that visual studio is selected by returning to **"Edit" ➞ "Preferences" ➞ "External Tools"** as in the previous step,<br/>
**otherwise**, select it again.

#### You can now [Start Scripting](#Starting-Scripting).

# Starting Scripting:
Before starting to create Scripts you must **create** a **"Scripts" folder** inside your mod folder next to other folders like **"Definitions"** or **"Prefabs"**.
#### **IMPORTANT**, ALWAYS PUT THE SCRIPTS AT A MINIMUM INSIDE YOUR MOD FOLDER OTHERWISE IT WILL NOT BE TAKEN INTO ACCOUNT WHEN BUILDING THE MOD.

![](https://github.com/guanaco0403/Guanaco-Firework-Mania-Mods/blob/main/Images/Scripting-Guide/Unity3.png)

**To create a script**, it's quite simple, you just have to right click inside the **"Scripts"** folder and select **"Create" ➞ "C# Script"**.<br/>
Then give it a **UNIQUE** name **(it is important that each script has a unique name)**, and you can then **double click** on it to open it in **visual studio 2019**.

You can now follow the getting started guide with [Unity scripting](#Unity-Scripting-Basics).

### IMPORTANT, to make the in-game script work, you need to associate it with a gameobject in a prefab like this:

![](https://github.com/guanaco0403/Guanaco-Firework-Mania-Mods/blob/main/Images/Scripting-Guide/Unity4.png)

# Unity Scripting Basics:
I will now explain the **BASIS** of scripting in **Unity**,<br/>
**First of all**, if you open a script, you will land on a **visual studio** page like below.

![](https://github.com/guanaco0403/Guanaco-Firework-Mania-Mods/blob/main/Images/Scripting-Guide/VS1.png)

There are two really important areas on this page,<br/>
First of all, the area where we will **write the lines of script**.

![](https://github.com/guanaco0403/Guanaco-Firework-Mania-Mods/blob/main/Images/Scripting-Guide/VS2.png)

And then the area where we see if our **script contains errors**.

![](https://github.com/guanaco0403/Guanaco-Firework-Mania-Mods/blob/main/Images/Scripting-Guide/VS3.png)
<br/>

### Now for the script itself,
This part of the script allows to include references to other unity functions like "UnityEngine" which is the reference of any script used in a unity game.

```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
```

This part of the script is its "class" and it's a bit like this zone of definition as a "house", it means that everything that happens inside this "class", belongs to it.<br/>
**IMPORTANT**, the class name must **ABSOLUTELY** be the same as the script file name.

```C#
public class ExampleScript : MonoBehaviour
{

}
```

This part of the script is a **"Start"** function and allows you to execute a sequence of script lines **ONLY once** and when the script is **started** (this is the area that we generally use to start the execution of ours script).

```C#
void Start()
{

}
```

This part of the script is an **"Update"** function and allows you to execute a series of script lines **AT EACH FRAME** of the game and is therefore quite practical to detect if something is happening in game with for example the keyboard.

```C#
void Update()
{

}
```

the **"{ }"** are used to **limit the area** where the lines of code of a function are **executed** (everything inside will be executed by the function and nothing outside).

the **";"** are placed at **each end of line of code** to tell the script to go to the **next line** once this line has been **executed**, **they are MANDATORY!!!**

the **"//"** are used to create **comments** in the script in order to find it, anything after the **"//"** on the same line will **not be executed**, it's just text.

#### For more information on how to get started with unity scripting, please go [here](https://unity.com/how-to/learning-c-sharp-unity-beginners).

# Fireworks Mania Scripting Functions:

**Fireworks Mania** has some functions of its own that can be used by the script to better interact for example with fireworks.
I will not go too far in the explanations because it could last hours or even days but I will give examples.

### Playing with Fuses

```C#
using FireworksMania.Core.Behaviors.Fireworks.Parts;
using UnityEngine;

public class Example_Fuse_Behavior : MonoBehaviour
{
    // Fireworks Mania Fuse Objects (Set it in the gameobject inspector of unity)
    public Fuse FireworkFuse;

    // Simple Variable that tells if the fuse is used
    private bool isUsed = false;

    // Update is called once per frame
    private void Update()
    {
        if (FireworkFuse.IsUsed == true && isUsed == false)
        {
            isUsed = true;
            // Execute something here ONE TIME when the Firework Is Used
        }
    }
}
```

```C#
using FireworksMania.Core.Behaviors.Fireworks.Parts;
using UnityEngine;

public class Example_Fuse_Behavior : MonoBehaviour
{
    // Fireworks Mania Fuse Objects (Set it in the gameobject inspector of unity)
    public Fuse FireworkFuse;

    // Simple Variable that tells if the fuse is used
    private bool isIgnited = false;

    // Update is called once per frame
    private void Update()
    {
        if (FireworkFuse.IsIgnited == true && isIgnited == false)
        {
            isIgnited = true;
            // Execute something here ONE TIME when the Firework Is Ignited
        }
    }
}
```

```C#
using FireworksMania.Core.Behaviors.Fireworks.Parts;
using UnityEngine;

public class Example_Fuse_Behavior : MonoBehaviour
{
    // Fireworks Mania Fuse Objects (Set it in the gameobject inspector of unity)
    public Fuse FireworkFuse;

    private void Start()
    {
        // Ignite the fuse at script start without using the lighter
        FireworkFuse.IgniteInstant();
    }
}
```

```C#
using FireworksMania.Core.Behaviors.Fireworks.Parts;
using UnityEngine;

public class Example_Fuse_Behavior : MonoBehaviour
{
    // Fireworks Mania Fuse Objects (Set it in the gameobject inspector of unity)
    public Fuse FireworkFuse;

    private void Start()
    {
        // Ignite the fuse at script start without using the lighter BUT WITHOUT FUSE TIME DELAY (Soo it directly launch the firework)
        FireworkFuse.IgniteWithoutFuseTime();
    }
}
```

### Playing with Player Controls

```C#
using FireworksMania.Core.Messaging;
using UnityEngine;

public class Example_Player_Script : MonoBehaviour
{
    //basic variable that contains if the player is frozen or not
    private bool Istriggered = false;
    void Update()
    {
        // if the Y key is pressed and the player is not frozen
        if (Input.GetKeyDown(KeyCode.Y) && Istriggered == false)
        {
            // Freeze the player and shows the mouse arrows (Useful to create UI)
            Messenger.Broadcast<MessengerEventChangeUIMode>(new MessengerEventChangeUIMode(true, false));

            // sets the variable as true (player frozen)
            Istriggered = true;
        }
        
        // else if the Y key is pressed and the player is frozen
        else if (Input.GetKeyDown(KeyCode.Y) && Istriggered == true)
        {
            // UnFreeze the player and hide the mouse arrows (Useful to create UI)
            Messenger.Broadcast<MessengerEventChangeUIMode>(new MessengerEventChangeUIMode(false, true));

            // sets the variable as true (player Unfrozen)
            Istriggered = false;
        }
    }
}
```

# Starting a Script at Mod Start:
In order to start your script automatically when your mod is loaded in game, you must use what is called a **"Startup Prefab Definition"** which will automatically load a Prefab in game in which your script will be associated.<br/>
**You can follow the video tutorial below to find out how.**<br/>
<br/>
the **"Sort Order"** parameter is optional, it just allows you to load the **StartupPrefabs** of all the mods in a certain way (the higher the value, the more your script will be loaded last).<br/>

https://user-images.githubusercontent.com/76651037/197382867-d12cee63-cdae-4249-bd5b-28c2adc6cb35.mp4

# Troubleshooting
you can use the "²" key next to the "1" key to open the in-game console, and from this console you can see any errors your script might have.<br/>
If the errors are Critical, they will be displayed in Red and if they are not very serious, they will be displayed in Orange.<br/>
<br/>
### Types of errors:
<br/>
- **NullReferenceException Error**
```
NullReferenceException: Object reference not set to an instance of an object
at Example.Start () [0x0000b] in /Unity/projects/nre/Assets/Example.cs:10 
```

# Bug Report, Question Or Suggestion:

If you have a question, a bug or if you have a request/suggestion the just [Create a issue](https://github.com/guanaco0403/Guanaco-Firework-Mania-Mods/issues/new/choose)
