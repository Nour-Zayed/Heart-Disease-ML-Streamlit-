import streamlit as st
import joblib
import numpy as np

model = joblib.load("model1.pkl")

# اختيار اللغة من الشريط الجانبي
language = st.sidebar.radio("🌐 اختر اللغة / Select Language", ["العربية", "English"])

# العناوين حسب اللغة
if language == "العربية":
    st.title("🔍 تطبيق التنبؤ بأمراض القلب 🩺")

    general_health_label = "🩺 التقييم العام للصحة"
    last_checkup_label = "📅 آخر موعد للفحص الطبي"
    physical_activity_label = "🏃‍♂️ هل تمارس الرياضة؟"
    sleep_hours_label = "😴 عدد ساعات النوم يومياً"
    heart_attack_label = "❤️ هل أصبت بنوبة قلبية من قبل؟"
    stroke_label = "🧠 هل أصبت بسكتة دماغية من قبل؟"
    asthma_label = "🌬️ هل تعاني من الربو؟"
    skin_cancer_label = "🦠 هل لديك سرطان الجلد؟"
    copd_label = "🫁 هل لديك مرض رئوي مزمن (COPD)؟"
    kidney_disease_label = "🩸 هل لديك مرض كلوي؟"
    diabetes_label = "🩸 هل لديك سكري؟"
    difficulty_walking_label = "🚶‍♂️ هل لديك صعوبة في المشي؟"
    smoker_status_label = "🚬 هل أنت مدخن؟"
    alcohol_drinkers_label = "🍷 هل تشرب الكحول؟"
    age_category_label = "📊 فئة العمر"
    bmi_category_label = "⚖️ فئة BMI"
    predict_button = "🔮 تنبؤ"
    safe_message = "✅ أنت في أمان من أمراض القلب!"
    risk_message = "⚠️ لديك احتمالية للإصابة بأمراض القلب!"
else:
    st.title("🔍 Heart Disease Prediction App 🩺")

    general_health_label = "🩺 General Health"
    last_checkup_label = "📅 Last Checkup"
    physical_activity_label = "🏃‍♂️ Do you exercise?"
    sleep_hours_label = "😴 Hours of sleep per day"
    heart_attack_label = "❤️ Had a heart attack before?"
    stroke_label = "🧠 Had a stroke before?"
    asthma_label = "🌬️ Do you have asthma?"
    skin_cancer_label = "🦠 Do you have skin cancer?"
    copd_label = "🫁 Do you have COPD?"
    kidney_disease_label = "🩸 Do you have kidney disease?"
    diabetes_label = "🩸 Do you have diabetes?"
    difficulty_walking_label = "🚶‍♂️ Difficulty walking?"
    smoker_status_label = "🚬 Are you a smoker?"
    alcohol_drinkers_label = "🍷 Do you drink alcohol?"
    age_category_label = "📊 Age category"
    bmi_category_label = "⚖️ BMI category"
    predict_button = "🔮 Predict"
    safe_message = "✅ You are safe from heart disease!"
    risk_message = "⚠️ You may be at risk of heart disease!"

# باقي النموذج
general_health = st.selectbox(general_health_label, ["Excellent", "Very Good", "Good", "Fair", "Poor"])
last_checkup_time = st.selectbox(last_checkup_label, ["Within past year", "Within past 2 years", "Within past 5 years", "5+ years ago", "Never"])
physical_activity = st.radio(physical_activity_label, ["No", "Yes"])
sleep_hours = st.slider(sleep_hours_label, 0, 24, 7)
heart_attack = st.radio(heart_attack_label, ["No", "Yes"])
stroke = st.radio(stroke_label, ["No", "Yes"])
asthma = st.radio(asthma_label, ["No", "Yes"])
skin_cancer = st.radio(skin_cancer_label, ["No", "Yes"])
copd = st.radio(copd_label, ["No", "Yes"])
kidney_disease = st.radio(kidney_disease_label, ["No", "Yes"])
diabetes = st.radio(diabetes_label, ["No", "Yes"])
difficulty_walking = st.radio(difficulty_walking_label, ["No", "Yes"])
smoker_status = st.radio(smoker_status_label, ["No", "Yes"])
alcohol_drinkers = st.radio(alcohol_drinkers_label, ["No", "Yes"])
age_category = st.selectbox(age_category_label, ["18-24", "25-29", "30-34", "35-39", "40-44", "45-49",
                                                 "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80 or older"])
bmi_category = st.selectbox(bmi_category_label, ["Underweight (<18.5)", "Normal (18.5-24.9)", "Overweight (25-29.9)", "Obese (30+)"])


# نفس دوال التشفير
def encode(value, yes_no=False):
    if yes_no:
        return 1 if value == "Yes" else 0
    return value

bmi_mapping = {
    "Underweight (<18.5)": 16,
    "Normal (18.5-24.9)": 22,
    "Overweight (25-29.9)": 27,
    "Obese (30+)": 32
}
bmi = bmi_mapping[bmi_category]

general_health_mapping = {"Excellent": 5, "Very Good": 4, "Good": 3, "Fair": 2, "Poor": 1}
general_health = general_health_mapping[general_health]

last_checkup_mapping = {"Within past year": 1, "Within past 2 years": 2, "Within past 5 years": 3, "5+ years ago": 4, "Never": 5}
last_checkup_time = last_checkup_mapping[last_checkup_time]

age_mapping = {"18-24": 0, "25-29": 1, "30-34": 2, "35-39": 3, "40-44": 4, "45-49": 5,
               "50-54": 6, "55-59": 7, "60-64": 8, "65-69": 9, "70-74": 10, "75-79": 11, "80 or older": 12}
age_category = age_mapping[age_category]

heart_attack = encode(heart_attack, yes_no=True)
stroke = encode(stroke, yes_no=True)
asthma = encode(asthma, yes_no=True)
skin_cancer = encode(skin_cancer, yes_no=True)
copd = encode(copd, yes_no=True)
kidney_disease = encode(kidney_disease, yes_no=True)
diabetes = encode(diabetes, yes_no=True)
difficulty_walking = encode(difficulty_walking, yes_no=True)
smoker_status = encode(smoker_status, yes_no=True)
alcohol_drinkers = encode(alcohol_drinkers, yes_no=True)
physical_activity = encode(physical_activity, yes_no=True)

input_data = np.array([[general_health, last_checkup_time, physical_activity, sleep_hours,
                        stroke, asthma, skin_cancer, copd, kidney_disease, diabetes,
                        difficulty_walking, smoker_status, age_category, bmi, alcohol_drinkers]])

if st.button(predict_button):
    prediction = model.predict(input_data)
    result = risk_message if prediction[0] == 1 else safe_message
    st.write(f"🔮 **{result}**")
