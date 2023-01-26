import bpy, os

# Specify the filepath of the scene file
scene_path = "./scene.blend"
output_path = "./renders/"
smpl_path = "./smpl_np.obj"

os.makedirs(output_path, exist_ok=True)


def render_image(cam_name, image_name):

	# Set the active camera
	bpy.context.scene.camera = bpy.data.objects[cam_name]
	
	# Set the render settings
	bpy.context.scene.render.filepath = output_path + "{}.png".format(image_name)
	bpy.context.scene.render.image_settings.file_format = 'PNG'

	# Render the scene
	bpy.ops.render.render(write_still=True)

def add_cam(cam_name, intrinsic, extrinsic):
	# Create a new camera object
	camera = bpy.data.cameras.new("cam_"+cam_name)

	# Create a new object for the camera
	camera_obj = bpy.data.objects.new(cam_name, camera)

	camera_obj.location = (1.0, 2.0, 3.0) # xyz

	# Link the camera object to the scene
	bpy.context.collection.objects.link(camera_obj)
	
	
def add_smpl(smpl_path):
	bpy.ops.import_scene.obj(filepath=smpl_path)


# Use the open_mainfile operator to load the scene
bpy.ops.wm.open_mainfile(filepath=scene_path)


add_smpl(smpl_path)


render_image("Camera", "render")



