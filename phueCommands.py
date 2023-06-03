from phue import Bridge

ip = 'bridge ip'
b = Bridge(ip)

# b.connect()

def setFull(group):
    b.set_group(group, 'bri', 254)

def set75(group):
    b.set_group(group, 'bri', 191)

def setHalf(group):
    b.set_group(group, 'bri', 127)

def setOff(group):
    b.set_group(group, 'bri', 0)

def getScenes():
    print(b.get_scene())

def setScene(group, scene):
    if scene == 'bye':
        scene = 'BI'
    b.run_scene(group, scene.capitalize())

# scenes = b.get_scene()
# # Print scene IDs and names
# for scene_id, scene in scenes.items():
#     print(f"Scene ID: {scene_id}, Name: {scene['name']}")
