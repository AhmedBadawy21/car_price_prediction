import streamlit as st
import pandas as pd
import joblib



def app():
    model_ML = joblib.load('modelXG.h5')
    st.title("Car price prediction")
    st.header("Used Car Price Project")

    st.write("This part predict the car price based on the following inputs:")


    levy = st.number_input("Enter the levy:",value = 0)
    Prod_year = st.number_input("Production year:",value = 0)
    eng_vol = st.number_input("Engine volume:" ,step=0.1,format="%.2f")
    mileage = st.number_input("Mileage:", value = 0)
    airbags = st.number_input("Airbags:", value = 0)
    wheels = st.radio("Wheels?",['Left wheel', 'Right-hand drive'])
    turbo = st.radio("Turbo?",['Yes', 'No'])

    df_color_map = pd.read_csv('df_color_map.csv').rename({'Unnamed: 0':'Address','0':'Number'},axis =1).set_index('Address').T.to_dict('list')
    color = st.selectbox("The color?:",['Silver', 'Black', 'White', 'Blue', 'Green', 'Grey', 'Red','Sky blue', 'Orange',\
        'Yellow', 'Golden', 'Beige', 'Brown','Carnelian red', 'Purple', 'Pink'])   # ==== Done ====
    color_num = df_color_map[color][0]

    leather_int = st.radio("Include leather interior?",['Yes','No'])

    df_fuel_map = pd.read_csv('df_fuel_map.csv').rename({'Unnamed: 0':'Address','0':'Number'},axis =1).set_index('Address').T.to_dict('list')
    fuel_type = st.selectbox("What is the fuel type?",['Hybrid', 'Petrol', 'Diesel', 'CNG', 'Plug-in Hybrid', 'LPG','Hydrogen'])  # ==== Done ====
    fuel_num = df_fuel_map[fuel_type][0]

    df_gear_map = pd.read_csv('df_gear_map.csv').rename({'Unnamed: 0':'Address','0':'Number'},axis =1).set_index('Address').T.to_dict('list')
    gear_type = st.selectbox("What is the gear box type?",['Automatic','Manual','Tiptronic','Variator']) # ==== Done ====
    gear_num = df_gear_map[gear_type][0]


    df_manuf_map = pd.read_csv('df_manuf_map.csv').rename({'Unnamed: 0':'Address','0':'Number'},axis =1).set_index('Address').T.to_dict('list')
    manuf = st.selectbox("What is the manufacturer?",df_manuf_map.keys())
    manuf_num = df_manuf_map[manuf][0]

    df_model_map = pd.read_csv('df_model_map.csv').rename({'Unnamed: 0':'Address','0':'Number'},axis =1).set_index('Address').T.to_dict('list')
    model = st.selectbox("What is the model?", df_model_map.keys())  # ==== Done ====
    model_num = df_model_map[model][0]


    df_category_map = pd.read_csv('df_category_map.csv').rename({'Unnamed: 0':'Address','0':'Number'},axis =1).set_index('Address').T.to_dict('list')
    car_category = st.selectbox("What is the car category?",['Jeep', 'Hatchback', 'Microbus', 'Sedan', \
        'Goods wagon','Universal', 'Coupe', 'Minivan', 'Cabriolet', 'Limousine','Pickup']) # ==== Done ====
    cat_num = df_category_map[car_category][0]

    age_num = 2020 - Prod_year

    predict = st.button("Predict")
    if predict:
        df = pd.DataFrame.from_dict(
            {
                'Levy':[levy], #ok
                'Prod. year':[Prod_year], #ok
                'Engine volume':[eng_vol], #ok
                'Mileage':[mileage], #ok
                'Airbags':[airbags], #ok
                'Wheel':[1 if wheels == "Left wheel" else 0], #easy
                'Turbo':[1 if turbo == "Yes" else 0], #easy
                'Color':[color_num], #map
                'Leather interior':[1 if leather_int == "Yes" else 0], #easy
                'Fuel type':[fuel_num], #map
                'Gear box type':[gear_num], #map
                'Manufacturer':[manuf_num], #map
                'Model':[model_num], #map
                'Category':[cat_num], #map
                'Age':[age_num] #map
                
            }
        )
        st.dataframe(df)
        pred = model_ML.predict(df)
        st.write(F"The prediction is:  {pred}")


app()