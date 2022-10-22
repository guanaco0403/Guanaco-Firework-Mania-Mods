![Icon Logo](https://avatars.githubusercontent.com/u/76651037?s=48&v=4)

---
Hello, This Guide will help you Starting Scripting Fireworks Mania mods in unity.<br/>
Please Keep in mind that scripting is not easy for beginers.<br/>
---
**Created by Guanaco0403**

Don't forget to join the [firework mania Discord Server](https://discord.gg/6TJPwUUrJp)

# Table of Contents

### • [First Scripting Setup](#First-Scripting-Setup)

### • [Unity Scripting Basics](#Mods-In-Development)

### • [Fireworks Mania Scripting Functions](#Bug-Report-Question-Or-Suggestion)
<br/>

# First Scripting Setup:

## Step 1
To start, you must have followed all the steps in order to configure unity for fireworks mania modding.<br/>
You can find this guide by [clicking here](https://github.com/Laumania/FireworksMania.ModTools#getting-started).

**IMPORTANT, MAKE SURE YOU CLOSED UNITY BEFORE GOING TO NEWXT STEP!!!**<br/>
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

You can now follow the getting started guide with [Unity scripting](https://github.com/Laumania/FireworksMania.ModTools#getting-started).

### IMPORTANT, to make the in-game script work, you need to associate it with a gameobject in a prefab like this:

# Bug Report, Question Or Suggestion:

If you have a question, a bug or if you have a request/suggestion the just [Create a issue](https://github.com/guanaco0403/Guanaco-Firework-Mania-Mods/issues/new/choose)
