import streamlit as st
import pandas as pd
import mysql.connector

# Title of the app
st.title("MY REDBUS APPLICATION")
st.subheader("Check out the video to book your tickets!")

st.video("https://www.youtube.com/watch?v=eyAAUGhvZu8")

def get_data_from_mysql():
    try:
        # Establish connection to the MySQL database
        conn = mysql.connector.connect(
            host="127.0.0.1",       # Replace with your host
            user="root",            # Replace with your MySQL username
            password="Geethu@2003", # Replace with your MySQL password
            database="redbus",      # Replace with your database name
            port=3306               # Replace with your port if different
        )
        
        # Fetch data from the table
        query = "SELECT * FROM bus_routes"
        df = pd.read_sql(query, conn)
        conn.close()
        
        return df
    
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return pd.DataFrame()
    
df = get_data_from_mysql()

if not df.empty:
    st.dataframe(df)  # Display the DataFrame as a table
else:
    st.write("No data found.")


# Sample data for the dropdown
options = [
    'Vijayawada to Hyderabad', 'Hyderabad to Vijayawada',
    'Kakinada to Visakhapatnam', 'Visakhapatnam to Kakinada',
    'Chittoor (Andhra Pradesh) to Bangalore', 'Kadapa to Bangalore',
    'Anantapur (andhra pradesh) to Bangalore', 'Tirupati to Bangalore',
    'Visakhapatnam to Vijayawada', 'Ongole to Hyderabad',
    'Khammam to Hyderabad', 'Hyderabad to Khammam',
    'Hyderabad to Srisailam', 'Karimnagar to Hyderabad',
    'Hyderabad to Nirmal', 'Hyderabad to Mancherial',
    'Hyderabad to Adilabad', 'Hyderabad to Karimnagar',
    'Kothagudem to Hyderabad', 'Bangalore to Kozhikode',
    'Kozhikode to Ernakulam', 'Kozhikode to Bangalore',
    'Ernakulam to Kozhikode', 'Kozhikode to Mysore',
    'Kozhikode to Thiruvananthapuram',
    'Bangalore to Kalpetta (kerala)', 'Mysore to Kozhikode',
    'Kalpetta (kerala) to Bangalore', 'Kozhikode to Thrissur',
    'Burdwan to Kolkata', 'Kolkata to Burdwan',
    'Durgapur (West Bengal) to Kolkata', 'Kolkata to Haldia',
    'Haldia to Kolkata', 'Kolkata to Durgapur (West Bengal)',
    'Kolkata to Arambagh (West Bengal)', 'Digha to Kolkata',
    'Kolkata to Digha', 'Kolkata to Bankura', 'Mandarmani to Kolkata',
    'Kolkata to Mandarmani', 'Kolkata to Bakkhali', 'Delhi to Shimla',
    'Shimla to Delhi', 'Manali to Chandigarh', 'Chandigarh to Manali',
    'Delhi to Manali', 'Hamirpur (Himachal Pradesh) to Chandigarh',
    'Delhi to Hamirpur (Himachal Pradesh)', 'Delhi to Chandigarh',
    'Manali to Delhi', 'Hamirpur (Himachal Pradesh) to Delhi',
    'Jodhpur to Ajmer', 'Beawar (Rajasthan) to Jaipur (Rajasthan)',
    'Udaipur to Jodhpur', 'Jaipur (Rajasthan) to Jodhpur',
    'Sikar to Jaipur (Rajasthan)', 'Kishangarh to Jaipur (Rajasthan)',
    'Aligarh (uttar pradesh) to Jaipur (Rajasthan)',
    'Jodhpur to Beawar (Rajasthan)',
    'Kota(Rajasthan) to Jaipur (Rajasthan)',
    'Jaipur (Rajasthan) to Aligarh (uttar pradesh)',
    'Tezpur to Guwahati', 'Guwahati to Tezpur',
    'Nagaon (Assam) to Guwahati', 'Guwahati to Nagaon (Assam)',
    'Goalpara to Guwahati', 'Jorhat to North Lakhimpur',
    'Dhubri to Guwahati', 'Guwahati to Dhubri',
    'North Lakhimpur to Sibsagar', 'North Lakhimpur to Jorhat'
]

def filter_options(search_term):
    """Filter options based on search input."""
    search_term = search_term.lower()
    if search_term == "":
        return options
    return [option for option in options if option.lower().startswith(search_term)]

# Title of the app
st.subheader('Dropdown with Search Option')

# Search input
search_term = st.text_input('Search:', '')

# Filter options based on search input
filtered_options = filter_options(search_term)

# Display dropdown with filtered options
if filtered_options:
    selected_option = st.selectbox('Select the route:', filtered_options)
    st.write(f'You selected: {selected_option}')
else:
    st.write('No options found.')

option = st.selectbox(
    "Select the rating of your bus",
    (3.3, 3.9, 3.1, 4.1, 3.8, 4.0, 4.4, 3.2, 3.0,
    4.7, 4.6, 4.5, 2.8, 3.4, 3.5, 4.3, 1.8, 3.7,
    2.9, 3.6, 2.4, 2.5, 1.9, 2.6, 2.3, 2.7, 4.2,
    1.5, 2.1, 0.0, 1.2, 4.8, 2.0, 1.0, 1.7, 4.9, 2.2,
    5.0, 1.6, 1.4, 1.3, 1.1)
)
bustype=st.selectbox("Select the Bus type",
        ('AMARAVATHI (VOLVO / SCANIA A.C Multi Axle)',
       'DOLPHIN CRUISE (VOLVO / SCANIA A.C Multi Axle)',
       'Super Luxury (Non AC Seater 2+2 Push Back)',
       'STAR LINER(NON-AC SLEEPER 2+1)', 'VENNELA (A.C. SLEEPER)',
       'INDRA(A.C. Seater)', 'A/C Seater / Sleeper (2+1)',
       'Electric A/C Seater (2+2)', 'Scania AC Multi Axle Sleeper (2+1)',
       'METRO LUXURY A/C', 'ULTRA DELUXE (NON-AC, 2+2 PUSH BACK)',
       'NON A/C Push Back (2+2)', 'A/C Sleeper (2+1)',
       'Non A/C Seater / Sleeper (2+1)', 'Express(Non AC Seater)',
       'NON A/C Seater (2+3)', 'NON A/C Sleeper (2+1)',
       'NON A/C Seater/ Sleeper (2+1)',
       'Volvo Multi-Axle I-Shift A/C Semi Sleeper (2+2)',
       'Volvo A/C B11R Multi Axle Semi Sleeper (2+2)',
       'Volvo Multi Axle A/C Sleeper I-Shift B11R (2+1)',
       'SAPTAGIRI EXPRESS', '', 'SUPER LUXURY (NON-AC, 2 + 2 PUSH BACK)',
       'RAJDHANI (A.C. Semi Sleeper)',
       'RAJADHANI AC (CONVERTED METRO LUXURY)', 'NON A/C Seater (2+2)',
       'Lahari A/C sleeper', 'NON A/C Hi-Tech (2+2)',
       'LAHARI A/C SLEEPER CUM SEATER',
       'Volvo Multi Axle B9R A/C Sleeper (2+1)',
       'Lahari Non A/C Sleeper Cum Seater',
       'Bharat Benz A/C Sleeper (2+1)', 'Bharat Benz A/C Seater (2+2)',
       'Volvo Multi-Axle A/C Semi Sleeper (2+2)', 'AC Sleeper (2+1)',
       'NON A/C Semi Sleeper (2+2)', 'Deluxe (Non AC Seater 2+2)',
       'Swift Deluxe Non AC Air Bus (2+2)',
       'Super Fast Non AC Seater (2+3)', 'SWIFT-GARUDA A/C SEATER BUS',
       'Super Express Non AC Seater Air Bus (2+2)',
       'VE A/C Seater / Sleeper (2+1)', 'VE A/C Sleeper (2+1)',
       'Low Floor AC Seater 2+2', 'AC MULTI AXLE',
       'Bharat Benz A/C Seater /Sleeper (2+1)',
       'A/C Seater/Sleeper (2+1)', 'A/C Semi Sleeper (2+2)',
       'NON AC Seater / Sleeper 2+1',
       'Bharat Benz A/C Semi Sleeper (2+2)', 'A/C Seater Push Back (2+2)',
       'Non AC Seater (2+3)', 'Volvo A/C Seater (2+2)',
       'Volvo B11R Multi Axle Seater (2+2)',
       'Volvo 9600 A/C Semi Sleeper (2+2)',
       'Volvo 9600 Multi Axle Semi-Sleeper (2+2)', 'AC Seater (2+2)',
       'AC Seater (2+3)', 'A/C Seater Push Back (2+3)',
       'A/C Seater (2+3)', 'A/C Seater / Sleeper (2+2)',
       'Volvo AC Seater (2+2)', 'Volvo 9600 A/C Seater (2+2)',
       'VE A/C Seater (2+2)', 'Non AC Seater (2+2)',
       'Ordinary 3+2 Non AC Seater', 'Himsuta AC Seater Volvo/Scania 2+2',
       'A/C Executive (2+3)', 'Volvo A/C Semi Sleeper (2+2 )',
       'Volvo A/C Semi Sleeper (2+2)',
       'Mercedes Multi-Axle Semi Sleeper (2+2)',
       'Volvo Multi-Axle I-Shift B11R Semi Sleeper (2+2)',
       'Scania Multi-Axle AC Semi Sleeper (2+2)',
       'Himmani Deluxe 2+2 Non AC Seater', 'A/C Seater (2+2)',
       'Super Luxury Volvo AC Seater Pushback 2+2',
       'Express Non AC Seater 2+3', 'NON AC Seater/ Sleeper (2+1)',
       'Bharat Benz A/C Seater (2+1)',
       'Bharat Benz A/C Seater / Sleeper (2+2)',
       'Ordinary Non AC Seater 2+3', 'NON A/C Seater Semi Sleeper (2+1)',
       'NON A/C Seater (2+1)', 'A/C Seater (2+1)',
       'Bharat Benz NON A/C Seater / Sleeper (2+1)')
)
st.write("You selected:", bustype)
price=st.selectbox("Choose your price range",
                   ('INR 720', 'INR 469', 'INR 670', 'INR 607', 'INR 781', 'INR 436',
       'INR 567', 'INR 543', '450', 'INR 419', 'INR 528', 'INR 839',
       'INR 621', 'INR 449', '500', 'INR 472', 'INR 340', 'INR 281',
       'INR 383', 'INR 269', 'INR 250', 'INR 239', 'INR 399', 'INR 660',
       'INR 499', 'INR 545', 'INR 890', 'INR 990', 'INR 170', 'INR 186',
       'INR 215', 'INR 304', '427', '314', '332', 'INR 649', 'INR 439',
       'INR 412', 'INR 526', 'INR 467', 'INR 460', 'INR 300', 'INR 750',
       'INR 450', 'INR 650', 'INR 307', 'INR 700', 'INR 900', 'INR 800',
       'INR 1100', 'INR 314', 'INR 294', '', 'INR 694', 'INR 605',
       'INR 624', 'INR 602', 'INR 590', 'INR 555', 'INR 320', 'INR 389',
       'INR 600', 'INR 380', 'INR 400', 'INR 610', 'INR 442', 'INR 343',
       'INR 283', 'INR 500', 'INR 1039', 'INR 790', 'INR 376', 'INR 407',
       'INR 456', '764', 'INR 329', 'INR 350', 'INR 429', 'INR 520',
       '924', 'INR 504', 'INR 532', 'INR 533', 'INR 611', 'INR 550',
       '351', '899', 'INR 548', 'INR 451', 'INR 396', 'INR 470',
       'INR 497', '780', 'INR 560', 'INR 640', 'INR 473', 'INR 627',
       'INR 1000', '808', 'INR 309', 'INR 278', 'INR 255', 'INR 494',
       '903', '902', 'INR 513', 'INR 688', 'INR 620', 'INR 950',
       'INR 949', 'INR 261', 'INR 288', 'INR 268', 'INR 299', 'INR 452',
       'INR 398', 'INR 319', 'INR 749', 'INR 723', 'INR 586', 'INR 742',
       'INR 565', 'INR 515', 'INR 904', 'INR 524', 'INR 377', 'INR 285',
       'INR 356', 'INR 849', 'INR 426', 'INR 253', 'INR 216', 'INR 181',
       'INR 762', 'INR 850', 'INR 100', 'INR 95', 'INR 155', 'INR 150',
       'INR 110', 'INR 97', 'INR 486', 'INR 145', 'INR 146', '285',
       'INR 370', '389', 'INR 420', '475', 'INR 410', '584', '370', '394',
       'INR 480', 'INR 185', '352', '257', '278', '299', '340', '405',
       'INR 1896', 'INR 1899', '2249', 'INR 230', 'INR 1199', '768',
       'INR 468', '540', '675', '809', 'INR 507', 'INR 892', 'INR 622',
       'INR 867', '712', '509', '569', '765', '555', '582', 'INR 490',
       'INR 920', 'INR 938', 'INR 549', 'INR 943', '664', '462', '474',
       'INR 975', 'INR 575', 'INR 580', '522', '495', 'INR 573',
       'INR 1446', 'INR 820', 'INR 822', 'INR 1428', 'INR 809', '647',
       'INR 541', 'INR 537', 'INR 318', 'INR 615', 'INR 344', '648',
       'INR 696', 'INR 608', 'INR 613', 'INR 1118', 'INR 574', 'INR 1008',
       'INR 604', 'INR 1093', '740', '759', 'INR 265', 'INR 270',
       'INR 280', 'INR 375', '380', 'INR 455', '508', 'INR 946', '673',
       '674', 'INR 909', '719', 'INR 1115', 'INR 229', 'INR 302',
       'INR 458', 'INR 330', 'INR 141', 'INR 211', 'INR 424', 'INR 282',
       'INR 475', 'INR 667', 'INR 363', 'INR 448', 'INR 740', 'INR 129',
       'INR 213', 'INR 123', 'INR 139', 'INR 260', 'INR 284.76',
       'INR 120', 'INR 184', 'INR 361', 'INR 476', 'INR 339', 'INR 167',
       'INR 235', 'INR 341', 'INR 369', 'INR 463', '400', '342')
)
st.write("You selected:", price)