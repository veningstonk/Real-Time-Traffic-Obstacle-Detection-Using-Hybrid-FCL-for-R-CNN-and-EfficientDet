# # 5 & 6
#
# def draw_keypoints_on_image_array(image,
#                                   keypoints,
#                                   color='red',
#                                   radius=2,
#                                   use_normalized_coordinates=True):
#   print("entered 5")
#   """Draws keypoints on an image (numpy array).
#   Args:
#     image: a numpy array with shape [height, width, 3].
#     keypoints: a numpy array with shape [num_keypoints, 2].
#     color: color to draw the keypoints with. Default is red.
#     radius: keypoint radius. Default value is 2.
#     use_normalized_coordinates: if True (default), treat keypoint values as
#       relative to the image.  Otherwise treat them as absolute.
#   """
#   image_pil = Image.fromarray(np.uint8(image)).convert('RGB')
#   draw_keypoints_on_image(image_pil, keypoints, color, radius,
#                           use_normalized_coordinates)
#   np.copyto(image, np.array(image_pil))
#
#
# def draw_keypoints_on_image(image,
#                             keypoints,
#                             color='red',
#                             radius=2,
#                             use_normalized_coordinates=True):
#   print("entered 6")
#   """Draws keypoints on an image.
#   Args:
#     image: a PIL.Image object.
#     keypoints: a numpy array with shape [num_keypoints, 2].
#     color: color to draw the keypoints with. Default is red.
#     radius: keypoint radius. Default value is 2.
#     use_normalized_coordinates: if True (default), treat keypoint values as
#       relative to the image.  Otherwise treat them as absolute.
#   """
#   draw = ImageDraw.Draw(image)
#   im_width, im_height = image.size
#   keypoints_x = [k[1] for k in keypoints]
#   keypoints_y = [k[0] for k in keypoints]
#   if use_normalized_coordinates:
#     keypoints_x = tuple([im_width * x for x in keypoints_x])
#     keypoints_y = tuple([im_height * y for y in keypoints_y])
#   for keypoint_x, keypoint_y in zip(keypoints_x, keypoints_y):
#     draw.ellipse([(keypoint_x - radius, keypoint_y - radius),
#                   (keypoint_x + radius, keypoint_y + radius)],
#                  outline=color, fill=color)
#
#
# def draw_mask_on_image_array(image, mask, color='red', alpha=0.7):
#   print("entered 7")
#   """Draws mask on an image.
#   Args:
#     image: uint8 numpy array with shape (img_height, img_height, 3)
#     mask: a float numpy array of shape (img_height, img_height) with
#       values between 0 and 1
#     color: color to draw the keypoints with. Default is red.
#     alpha: transparency value between 0 and 1. (default: 0.7)
#   Raises:
#     ValueError: On incorrect data type for image or masks.
#   """
#   if image.dtype != np.uint8:
#     raise ValueError('`image` not of type np.uint8')
#   if mask.dtype != np.float32:
#     raise ValueError('`mask` not of type np.float32')
#   if np.any(np.logical_or(mask > 1.0, mask < 0.0)):
#     raise ValueError('`mask` elements should be in [0, 1]')
#   rgb = ImageColor.getrgb(color)
#   pil_image = Image.fromarray(image)
#
#   solid_color = np.expand_dims(
#       np.ones_like(mask), axis=2) * np.reshape(list(rgb), [1, 1, 3])
#   pil_solid_color = Image.fromarray(np.uint8(solid_color)).convert('RGBA')
#   pil_mask = Image.fromarray(np.uint8(255.0*alpha*mask)).convert('L')
#   pil_image = Image.composite(pil_solid_color, pil_image, pil_mask)
#   np.copyto(image, np.array(pil_image.convert('RGB')))
#
#
# # 3 & 4
# def draw_bounding_boxes_on_image_array(image,
#                                        boxes,
#                                        color='red',
#                                        thickness=4,
#                                        display_str_list_list=()):
#   print("entered 3")
#   """Draws bounding boxes on image (numpy array).
#   Args:
#     image: a numpy array object.
#     boxes: a 2 dimensional numpy array of [N, 4]: (ymin, xmin, ymax, xmax).
#            The coordinates are in normalized format between [0, 1].
#     color: color to draw bounding box. Default is red.
#     thickness: line thickness. Default value is 4.
#     display_str_list_list: list of list of strings.
#                            a list of strings for each bounding box.
#                            The reason to pass a list of strings for a
#                            bounding box is that it might contain
#                            multiple labels.
#   Raises:
#     ValueError: if boxes is not a [N, 4] array
#   """
#   image_pil = Image.fromarray(image)
#   draw_bounding_boxes_on_image(image_pil, boxes, color, thickness,
#                                display_str_list_list)
#   np.copyto(image, np.array(image_pil))
#
#
# def draw_bounding_boxes_on_image(image,
#                                  boxes,
#                                  color='red',
#                                  thickness=4,
#                                  display_str_list_list=()):
#   print("entered 4")
#   """Draws bounding boxes on image.
#   Args:
#     image: a PIL.Image object.
#     boxes: a 2 dimensional numpy array of [N, 4]: (ymin, xmin, ymax, xmax).
#            The coordinates are in normalized format between [0, 1].
#     color: color to draw bounding box. Default is red.
#     thickness: line thickness. Default value is 4.
#     display_str_list_list: list of list of strings.
#                            a list of strings for each bounding box.
#                            The reason to pass a list of strings for a
#                            bounding box is that it might contain
#                            multiple labels.
#   Raises:
#     ValueError: if boxes is not a [N, 4] array
#   """
#   boxes_shape = boxes.shape
#   if not boxes_shape:
#     return
#   if len(boxes_shape) != 2 or boxes_shape[1] != 4:
#     raise ValueError('Input must be of size [N, 4]')
#   for i in range(boxes_shape[0]):
#     display_str_list = ()
#     if display_str_list_list:
#       display_str_list = display_str_list_list[i]
#     draw_bounding_box_on_image(image, boxes[i, 0], boxes[i, 1], boxes[i, 2],
#                                boxes[i, 3], color, thickness, display_str_list)
