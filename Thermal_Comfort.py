import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
@st.cache
def load_data():
    data = pd.read_csv('ashrae_db2.01.csv', encoding='ISO-8859-1', on_bad_lines='skip')
    return data

# Load the data
data = load_data()

# Handle NaN in 'Building type' and 'Country' by filling with 'Unknown'
data['Building type'] = data['Building type'].fillna('Unknown')
data['Country'] = data['Country'].fillna('Unknown')

# Sidebar for filtering
st.sidebar.title('Filter Options')

# Dropdown for selecting Building Type
building_type = st.sidebar.selectbox(
    'Select Building Type', data['Building type'].unique())

# Dropdown for selecting Cooling Strategy
cooling_strategy = st.sidebar.selectbox(
    'Select Cooling Strategy', data['Cooling startegy_building level'].unique())

# Dropdown for selecting Country
country = st.sidebar.selectbox(
    'Select Country', data['Country'].unique())

# Filter data based on sidebar options
filtered_data = data[
    (data['Building type'] == building_type) &
    (data['Cooling startegy_building level'] == cooling_strategy) &
    (data['Country'] == country)
]

# Main dashboard title
st.title('Thermal Comfort Analysis Dashboard')

# Scatter Plot: Air Temperature vs. Thermal Comfort
st.subheader(f'Scatter Plot: Air Temperature vs. Thermal Comfort for {building_type} buildings in {country}')
fig = px.scatter(filtered_data, x='Air temperature (¡C)', y='Thermal comfort',
                 color='Thermal sensation', title='Thermal Comfort vs Air Temperature')
st.plotly_chart(fig)

# Bar Chart: Thermal Comfort by Season
st.subheader(f'Bar Chart: Thermal Comfort by Season for {building_type} buildings in {country}')
fig = px.bar(filtered_data, x='Season', y='Thermal comfort', color='Thermal comfort',
             title='Thermal Comfort across Seasons')
st.plotly_chart(fig)

# Histogram: Distribution of Thermal Comfort
st.subheader(f'Histogram: Distribution of Thermal Comfort for {building_type} buildings in {country}')
fig = px.histogram(filtered_data, x='Thermal comfort', nbins=20,
                   title='Distribution of Thermal Comfort Ratings')
st.plotly_chart(fig)

# Points related to building materials and design based on cooling strategy and building type
st.subheader('Building Materials Requirements for Thermal Comfort')

# Define building types and cooling strategies combinations
if building_type == "Classroom":
    if cooling_strategy == "Air Conditioned":
        st.markdown("""
        ### Classroom - Air Conditioned
        1. **Insulation**: 
           - Use high-performance insulation to minimize thermal loss.
        2. **Window Treatments**: 
           - Install solar control blinds to reduce glare and heat gain.
        3. **Air Quality**: 
           - Use high-efficiency filters in HVAC systems to ensure good air quality.
        4. **Acoustic Materials**: 
           - Incorporate sound-absorbing materials to enhance the learning environment.
        """)

    elif cooling_strategy == "Naturally Ventilated":
        st.markdown("""
        ### Classroom - Naturally Ventilated
        1. **Operable Windows**: 
           - Design for maximum cross-ventilation.
        2. **Ceiling Fans**: 
           - Install ceiling fans to improve air circulation.
        3. **Thermal Mass**: 
           - Use materials with high thermal mass to stabilize temperatures.
        4. **Shading Devices**: 
           - Implement shading devices to reduce solar heat gain.
        """)

    elif cooling_strategy == "Mixed Mode":
        st.markdown("""
        ### Classroom - Mixed Mode
        1. **Flexible HVAC System**: 
           - Ensure the system can switch between natural and mechanical ventilation.
        2. **Monitoring Systems**: 
           - Use sensors to monitor temperature and air quality for optimal comfort.
        3. **Daylight Maximization**: 
           - Design windows for daylighting while minimizing heat gain.
        4. **Adjustable Shading**: 
           - Include adjustable shades to enhance comfort and reduce glare.
        """)

    elif cooling_strategy == "Mechanically Ventilated":
        st.markdown("""
        ### Classroom - Mechanically Ventilated
        1. **Duct Design**: 
           - Ensure ducts are properly sized and insulated to reduce energy loss.
        2. **Zoning**: 
           - Implement zoning controls for different areas of the classroom.
        3. **Regular Maintenance**: 
           - Schedule regular maintenance of HVAC systems for optimal performance.
        4. **Noise Control**: 
           - Use sound-absorbing materials to minimize noise from HVAC systems.
        """)

# Repeat similar blocks for other building types (Office, Others, Multifamily housing, Senior center)

if building_type == "Office":
    if cooling_strategy == "Air Conditioned":
        st.markdown("""
        ### Office - Air Conditioned
        1. **Insulation**: 
           - Use high R-value insulation in walls and roofs to minimize heat loss.
        2. **Window Treatments**: 
           - Apply solar control films or shades to reduce solar gain.
        3. **Thermal Mass**: 
           - Incorporate materials with high thermal mass in common areas to stabilize indoor temperatures.
        4. **Airflow Management**: 
           - Design an efficient HVAC system with variable air volume (VAV) for tailored comfort.
        """)

    elif cooling_strategy == "Naturally Ventilated":
        st.markdown("""
        ### Office - Naturally Ventilated
        1. **Natural Light**: 
           - Design windows to maximize natural light while minimizing heat.
        2. **Operable Windows**: 
           - Provide operable windows for user control over ventilation.
        3. **Low-VOC Materials**: 
           - Use low-VOC materials to maintain air quality.
        4. **Green Spaces**: 
           - Integrate indoor plants for improved air quality and comfort.
        """)

    elif cooling_strategy == "Mixed Mode":
        st.markdown("""
        ### Office - Mixed Mode
        1. **HVAC Integration**: 
           - Ensure HVAC systems work seamlessly with natural ventilation.
        2. **User Controls**: 
           - Provide users with controls to adjust settings based on comfort.
        3. **Monitoring Systems**: 
           - Use sensors to adapt the system based on occupancy and outdoor conditions.
        4. **Acoustic Treatments**: 
           - Incorporate acoustic panels to reduce noise in open office spaces.
        """)

    elif cooling_strategy == "Mechanically Ventilated":
        st.markdown("""
        ### Office - Mechanically Ventilated
        1. **Zoning Systems**: 
           - Implement zoning controls to tailor cooling to different areas based on usage.
        2. **Duct Sealing**: 
           - Ensure ductwork is sealed and insulated to prevent energy loss.
        3. **Regular Maintenance**: 
           - Schedule regular HVAC maintenance to ensure optimal performance.
        4. **Air Quality Management**: 
           - Use CO2 sensors to monitor and manage indoor air quality.
        """)

# Add similar blocks for "Others", "Multifamily housing", and "Senior center"

if building_type == "Others":
    if cooling_strategy == "Air Conditioned":
        st.markdown("""
        ### Others - Air Conditioned
        1. **Insulation**: 
           - Select appropriate insulation materials to improve energy efficiency.
        2. **Air Quality**: 
           - Install high-efficiency HVAC filters for improved air quality.
        3. **Window Design**: 
           - Use double-glazed windows to minimize heat transfer.
        4. **Zoning**: 
           - Create zones in large spaces for tailored comfort.
        """)

    elif cooling_strategy == "Naturally Ventilated":
        st.markdown("""
        ### Others - Naturally Ventilated
        1. **Cross Ventilation**: 
           - Ensure design allows for effective cross ventilation.
        2. **Shading Devices**: 
           - Install shading devices to reduce solar heat gain.
        3. **Natural Materials**: 
           - Use natural materials that have good thermal performance.
        4. **User Control**: 
           - Provide operable windows for user control over comfort.
        """)

    elif cooling_strategy == "Mixed Mode":
        st.markdown("""
        ### Others - Mixed Mode
        1. **Hybrid Systems**: 
           - Use hybrid systems to balance mechanical and natural ventilation.
        2. **User Feedback**: 
           - Incorporate user feedback for comfort adjustments.
        3. **Performance Monitoring**: 
           - Regularly monitor system performance for optimization.
        4. **Flexible Design**: 
           - Design spaces to adapt to changing needs and climate.
        """)

    elif cooling_strategy == "Mechanically Ventilated":
        st.markdown("""
        ### Others - Mechanically Ventilated
        1. **Duct Insulation**: 
           - Insulate ductwork to minimize energy loss.
        2. **Regular Maintenance**: 
           - Schedule maintenance to ensure efficient operation.
        3. **Air Quality Monitoring**: 
           - Install sensors for continuous air quality monitoring.
        4. **User Controls**: 
           - Provide users with control options for comfort adjustments.
        """)

if building_type == "Multifamily housing":
    if cooling_strategy == "Air Conditioned":
        st.markdown("""
        ### Multifamily Housing - Air Conditioned
        1. **Insulation**: 
           - Use high-performance insulation in walls and ceilings to minimize heat transfer.
        2. **Shared HVAC Systems**: 
           - Design HVAC systems that effectively serve multiple units.
        3. **Noise Control**: 
           - Incorporate soundproofing materials between units for privacy.
        4. **Energy Efficiency**: 
           - Consider energy-efficient appliances in each unit.
        """)

    elif cooling_strategy == "Naturally Ventilated":
        st.markdown("""
        ### Multifamily Housing - Naturally Ventilated
        1. **Window Design**: 
           - Use operable windows in living spaces for natural airflow.
        2. **Outdoor Spaces**: 
           - Design balconies and terraces to enhance outdoor living.
        3. **Green Spaces**: 
           - Incorporate landscaping to provide shade and cooling.
        4. **Community Design**: 
           - Create communal areas that promote cross ventilation.
        """)

    elif cooling_strategy == "Mixed Mode":
        st.markdown("""
        ### Multifamily Housing - Mixed Mode
        1. **Flexible HVAC**: 
           - Design HVAC systems that can utilize both natural and mechanical ventilation.
        2. **User Controls**: 
           - Allow individual unit controls for personalization of comfort.
        3. **Energy Monitoring**: 
           - Implement systems to monitor energy usage for optimization.
        4. **Shared Amenities**: 
           - Design shared spaces for community engagement and comfort.
        """)

    elif cooling_strategy == "Mechanically Ventilated":
        st.markdown("""
        ### Multifamily Housing - Mechanically Ventilated
        1. **Duct System Design**: 
           - Ensure duct systems are efficiently designed to minimize energy loss.
        2. **Maintenance Access**: 
           - Provide easy access for regular maintenance of mechanical systems.
        3. **Ventilation Control**: 
           - Implement ventilation controls to manage airflow across multiple units.
        4. **Indoor Air Quality**: 
           - Use advanced filtration systems to maintain good indoor air quality.
        """)

if building_type == "Senior center":
    if cooling_strategy == "Air Conditioned":
        st.markdown("""
        ### Senior Center - Air Conditioned
        1. **Accessible Controls**: 
           - Provide easy-to-use controls for HVAC systems.
        2. **Comfort Zones**: 
           - Create comfortable areas with controlled temperatures.
        3. **Air Quality Filters**: 
           - Utilize high-efficiency air filters to improve indoor air quality.
        4. **Emergency Backup**: 
           - Ensure systems have backup power for extreme weather.
        """)

    elif cooling_strategy == "Naturally Ventilated":
        st.markdown("""
        ### Senior Center - Naturally Ventilated
        1. **Window Operation**: 
           - Ensure windows are easy to operate for residents.
        2. **Outdoor Access**: 
           - Design access to gardens and outdoor areas for fresh air.
        3. **Low Barrier Designs**: 
           - Use low barriers for easy access to outdoor areas.
        4. **Sun Control**: 
           - Install sun control devices to prevent overheating.
        """)

    elif cooling_strategy == "Mixed Mode":
        st.markdown("""
        ### Senior Center - Mixed Mode
        1. **Flexible System Design**: 
           - Design systems that easily switch between ventilation modes.
        2. **User Comfort**: 
           - Provide personal controls for temperature adjustments.
        3. **Temperature Monitoring**: 
           - Implement systems to monitor and adjust indoor temperatures.
        4. **Community Spaces**: 
           - Design community areas that facilitate airflow and comfort.
        """)

    elif cooling_strategy == "Mechanically Ventilated":
        st.markdown("""
        ### Senior Center - Mechanically Ventilated
        1. **Regular Maintenance**: 
           - Schedule regular maintenance for all mechanical systems.
        2. **Noise Control**: 
           - Incorporate sound-absorbing materials to reduce noise from HVAC.
        3. **Air Quality Monitoring**: 
           - Use sensors to monitor air quality and adjust systems accordingly.
        4. **User-Friendly Design**: 
           - Design user-friendly interfaces for HVAC controls.
        """)

# You can continue to add more sections or details for other building types and cooling strategies
