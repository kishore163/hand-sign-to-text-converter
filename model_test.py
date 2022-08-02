def load_test_data():
    images = []
    names = []
    size = 64,64
    for image in os.listdir(test_dir):
        temp = cv2.imread(test_dir + '/' + image)
        temp = cv2.resize(temp, size)
        images.append(temp)
        names.append(image)
    images = np.array(images)
    images = images.astype('float32')/255.0
    return images, names

test_images, test_img_names = load_test_data()

for i in range(len(test_img_names)):
    if test_img_names[i]=="nothing_test.jpg":
        test_img_names[i]=labels_dict['nothing']
        continue
    if test_img_names[i]=="space_test.jpg":
        test_img_names[i]=labels_dict['nothing']
        continue
    test_img_names[i]=labels_dict[test_img_names[i][0]]
print(test_img_names)

 
test_img_names = keras.utils.to_categorical(test_img_names)

model.evaluate(test_images,test_img_names)

def get_labels_for_plot(predictions):
    predictions_labels = []
    for i in range(len(predictions)):
        for ins in labels_dict:
            if predictions[i] == labels_dict[ins]:
                predictions_labels.append(ins)
                break
    return predictions_labels

predictions_labels_plot = get_labels_for_plot(predictions)
