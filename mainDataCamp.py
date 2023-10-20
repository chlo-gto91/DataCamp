import numpy as np
import streamlit as st
from PIL import Image
from keras.models import load_model
from keras.preprocessing.image import img_to_array



# Disable a deprecation warning
st.set_option('deprecation.showfileUploaderEncoding', False)

def predict(image_to_test):
    
    # Load the pre-trained machine learning model for eye disease prediction
    model = load_model('model_ML_data_camp_eyes.h5')
    
    # Open and preprocess the uploaded image
    image = Image.open(image_to_test).convert('RGB')
    image = image.resize((224, 224))
    image = img_to_array(image)
    image = image.reshape(1, 224, 224, 3)
    image = image / 255.0
    
    # Make a prediction using the model
    result = model.predict(image)
    result = np.argmax(result, axis=1)

    
    # Display the prediction result
    if result == 1:
       return st.success("The patient is healthy")
    else:
       return st.error("The patient is ill")


# Page Title
st.title("Eye Disease Information and Prevention")

# Sidebar content with logo and credits
st.sidebar.image("logo.png")
st.sidebar.markdown("# I-CARE")
# Navigation
page = st.sidebar.selectbox("Select a page:", ["Home", "Common Eye Diseases", "Prevention", "Symptoms", "Let's look at the statistics"])

# Home Page
if page == "Home":
    st.header("Welcome to the Eye Disease Information Center")
    st.write("This page provides information on common eye diseases, prevention tips, and what to do if you experience symptoms.")
    
# Common Eye Diseases Page
elif page == "Common Eye Diseases":
    st.header("Common Eye Diseases")
    st.write("Here are some common eye diseases:")
    st.write("- Age-Related Macular Degeneration (ARMD)")
    st.write("- Glaucoma")
    st.write("- Cataracts")
    st.write("- Dry eye")
    st.write("- Coloboma of the optic disc")
    st.write("- Age-related macular degeneration")
    st.write("- Branch retinal vein occlusion")
    st.write("- Optic disc pits")
    st.write("- Central retinal vein occlusion")
    st.write("- Choroidal neovascularization")
    st.write("- Retinitis pigmentosa")
    st.write("- Central serous retinopathy")
    st.write("- Hypertension retinopathy")
    st.write("- Presence of media haze")
    st.write("- Presence of tessellation")
    st.write("- Presence of drusen")
    st.write("- Presence of myopia")
    st.write("- Optic disc edema")
    
    
# Prevention Page
elif page == "Prevention":
    st.header("Prevention Tips")
    st.write("To maintain good eye health, consider the following tips:")
    st.write("1. Eat a diet rich in fruits and vegetables.")
    st.write("2. Protect your eyes from UV rays with sunglasses.")
    st.write("3. Maintain a healthy lifestyle with regular exercise.")
    st.write("4. Stay hydrated: Drink an adequate amount of water daily to help prevent dry eyes.")
    st.write("5. Follow the 20-20-20 Rule: Take a 20-second break every 20 minutes of screen time and look at something 20 feet away.")
    st.write("6. Schedule regular eye check-ups with an eye specialist or optometrist to catch and address any issues early.")
    st.write("7. Use protective eyewear when engaging in activities that could lead to eye injuries.")
    st.write("8. Reduce prolonged exposure to digital screens and adjust screen settings to reduce eye strain.")
    st.write("9. Consume foods rich in eye-healthy nutrients.")
    st.write("10. Quit smoking to reduce the risk of eye diseases.")
    st.write("11. Ensure proper lighting when reading or working to reduce eye strain.")
    st.write("12. Control underlying health conditions like diabetes and hypertension.")
    st.write("13. Wear protective eyewear in environments with potential eye hazards.")
    st.write("14. Shield your eyes from harmful UV rays by wearing UV-blocking sunglasses.")
    st.write("15. Moderate alcohol intake, as excessive consumption can lead to eye issues.")
    st.write("16. Stay active and engage in regular exercise to improve blood circulation to the eyes.")
    st.write("17. Avoid excessive eye rubbing to prevent introducing dirt and bacteria.")

    
# Symptoms Page
elif page == "Symptoms":
    st.header("Eye Disease Symptoms")
    st.write("If you experience any of the following symptoms, consult an eye specialist:")
    st.write("- Blurry vision")
    st.write("- Eye pain or discomfort")
    st.write("- Redness or irritation")
    st.write("- Excessive tearing or discharge")
    st.write("- Sensitivity to light (photophobia)")
    st.write("- Double vision")
    st.write("- Seeing halos around lights")
    st.write("- Floating spots or specks in your vision")
    st.write("- Gradual loss of peripheral vision")
    st.write("- Sudden loss of vision in one or both eyes")
    st.write("- Changes in the color of the iris")
    st.write("- Crossed or misaligned eyes (strabismus)")
    st.write("- Persistent eye fatigue or strain")
    st.write("- Persistent itching or burning sensation")
    st.write("- Frequent changes in eyeglass or contact lens prescriptions")
    st.write("- Unexplained changes in the appearance of the eyes or eyelids")

# Numbers Page
elif page=="Let's look at the statistics":
    st.header("Some statistics on eye diseases")
    st.write("In 2019 the WHO produced its first World Report on Vision, here is what it revealed:")
    st.write("- More than a Billion People Affected: At least 2.2 billion people are affected by visual impairment or blindness, among these cases more than a billion could have been avoided or are still not treated")
    st.write("- Common Conditions: Eye conditions and vision disorders, such as cataracts, trachoma, and refractive errors, are widespread, but often untreated.")
    st.write("- Unequal Distribution: The burden of eye conditions and visual impairment is not distributed equitably. Rural, low-income, women, older people, people with disabilities, ethnic minorities and indigenous populations are most affected.")
    st.write("- Unmet need for correction: In low- and middle-income areas, unmet need for distance vision correction is four times higher than in high-income areas.")
    st.write("- Increasing Blindness: In some low- and middle-income regions in sub-Saharan Africa and South Asia, the rate of blindness is eight times higher than in high-income countries.")
    st.write("- Funding Need: It is estimated that approximately $14.3 billion is needed to treat one billion people with visual impairments due to myopia, presbyopia or cataracts.")
    st.write("- Growth Factors: Population growth and the aging of the population increase the risk of developing eye disorders and visual impairment. The prevalence increases with age.")
    st.write("- Myopia: Reduced time spent outdoors and increased near vision activities increase the number of people with myopia.")
    st.write("- Diabetic Retinopathy: Diabetes, particularly type 2, can impact vision. Almost all diabetics will develop retinopathy at some point in their life.")
    st.write("- Late Detection: Due to lack of integration of eye care services, many people do not have access to regular examinations for early detection of diseases and appropriate treatment.")
    # Application title
    st.title('Eye Health Screening Test')
    # Question about the last screening visit
    last_checkup = st.radio("When was your last eye screening?", 
        options=["Less than 6 months ago", "Between 6 months and 1 year ago", "Over a year ago"])
    # Logic to display the appropriate message
    if last_checkup == "Less than 6 months ago":
        st.success("Congratulations! You had a recent eye screening.")
    elif last_checkup == "Between 6 months and 1 year ago":
        st.warning("It's recommended to have regular eye screenings to maintain good eye health.")
        st.write("In the meantime, you can use our AI to check the condition of your eyes.")
    else:
        st.warning("It's important to schedule an eye screening soon to maintain good eye health.")
        st.write("You can also use our AI to check the condition of your eyes.")




# Run the app
if __name__ == "__main__":
    st.sidebar.title("Eye Disease Information")
    st.sidebar.write("Learn about eye diseases and how to protect your vision.")
    st.sidebar.write("Select a page from the sidebar.")

# Set the title and subheader for the Streamlit app
st.title('Do you have an eye disease?')
st.subheader('Give us an image of your eye, and we will predict whether your eye is diseased or not.')

# Upload an image for prediction
image = st.file_uploader('Upload your image here', type=['jpg', 'jpeg', 'png'])
if image is not None:
    st.image(Image.open(image))
    st.markdown("See the result")

    # Button to trigger the prediction
    if st.button('Here'):
        with st.spinner(text="Work in Progress"):
            (predict(image))



# Footer
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text("Developed by I - care")
st.sidebar.text("Created by Chloé GATTINO,\nCarla HAMEURY, and Marie MICHOT")