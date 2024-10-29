import streamlit as st
import pandas as pd
from datetime import datetime, time

def main():
    st.set_page_config(page_title="Tarkov Raid Planner", layout="wide")
    st.title("Escape from Tarkov Raid Planner")

    # Sidebar for main category selection
    category = st.sidebar.selectbox(
        "Select Category",
        ["Loadout", "Maps", "Raid Info", "Items Database"]
    )

    if category == "Loadout":
        display_loadout_section()
    elif category == "Maps":
        display_maps_section()
    elif category == "Raid Info":
        display_raid_info()
    else:
        display_items_database()

def display_loadout_section():
    st.header("Loadout Builder")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Protection")
        helmet = st.selectbox("Helmet", [
            "None",
            "ULACH",
            "TC-2002",
            "Altyn",
            "FAST MT",
            "Airframe"
        ])
        
        headset = st.selectbox("Headset", [
            "None",
            "ComTac 2",
            "Sordin",
            "GSSH-01",
            "Razor"
        ])
        
        glasses = st.selectbox("Glasses", [
            "None",
            "Round glasses",
            "Anti-fragmentation glasses",
            "Crossbow tactical glasses"
        ])
        
        armor = st.selectbox("Armor", [
            "None",
            "PACA",
            "6B23-1",
            "Korund-VM",
            "GHZEL-K",
            "Slick"
        ])
        
        rig = st.selectbox("Tactical Rig", [
            "None",
            "Bank Robber",
            "MK3",
            "TV-110",
            "AVS"
        ])
        
        backpack = st.selectbox("Backpack", [
            "None",
            "MBSS",
            "Berkut",
            "Tri-Zip",
            "Attack 2",
            "Raid"
        ])

    with col2:
        st.subheader("Weapons")
        primary_weapon = st.selectbox("Primary Weapon", [
            "None",
            "M4A1",
            "AK-74N",
            "HK416A5",
            "Vector",
            "MP7A2"
        ])
        
        st.subheader("Weapon Mods")
        suppressor = st.checkbox("Suppressor")
        grip = st.selectbox("Pistol Grip", [
            "Standard",
            "RK-1",
            "Shift",
            "RVG",
            "Skeletonized"
        ])
        
        st.subheader("Equipment")
        grenades = st.multiselect("Grenades", [
            "F-1",
            "RGD-5",
            "M67",
            "Zarya",
            "Flash"
        ])
        
        container = st.selectbox("Secure Container", [
            "Alpha",
            "Beta",
            "Gamma",
            "Epsilon",
            "Kappa"
        ])

def display_maps_section():
    st.header("Maps")
    
    selected_map = st.selectbox("Select Map", [
        "Customs",
        "Woods",
        "Interchange",
        "Reserve",
        "Shoreline",
        "Factory",
        "Labs"
    ])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Map Information")
        st.write(f"Selected map: {selected_map}")
        st.write("Key Extracts:")
        if selected_map == "Customs":
            st.write("- ZB-1011")
            st.write("- ZB-1012")
            st.write("- Crossroads")
            st.write("- Trailer Park")
            st.write("- Old Gas Station (conditional)")
        
        st.write("Points of Interest:")
        if selected_map == "Customs":
            st.write("- Dorms")
            st.write("- New Gas")
            st.write("- Old Gas")
            st.write("- Fortress")
            st.write("- Big Red")

    with col2:
        st.subheader("Map Keys")
        if selected_map == "Customs":
            st.write("- Marked Room Key")
            st.write("- Factory Key")
            st.write("- Cabinet Key")
            st.write("- Customs Office Key")

def display_raid_info():
    st.header("Raid Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        raid_type = st.radio("Raid Type", ["PMC", "Scav"])
        time_of_day = st.radio("Time of Day", ["Day", "Night"])
        
        if raid_type == "PMC":
            st.subheader("PMC Settings")
            faction = st.radio("Faction", ["USEC", "BEAR"])
            level = st.number_input("PMC Level", min_value=1, max_value=99, value=1)
    
    with col2:
        st.subheader("Raid Timer")
        if raid_type == "PMC":
            raid_time = st.slider("Raid Duration (minutes)", 
                                min_value=20, 
                                max_value=45, 
                                value=35)
        else:
            raid_time = st.slider("Scav Raid Time Remaining (minutes)", 
                                min_value=10, 
                                max_value=35, 
                                value=20)

def display_items_database():
    st.header("Items Database")
    
    item_category = st.selectbox("Item Category", [
        "Barter Items",
        "Keys",
        "Provisions",
        "Medical",
        "Ammunition"
    ])
    
    if item_category == "Barter Items":
        st.dataframe({
            'Item': ['Bolts', 'Screws', 'Wires', 'CPU', 'GPU'],
            'Trader Value': ['₽8,000', '₽9,000', '₽12,000', '₽45,000', '₽180,000'],
            'Used In': ['Hideout', 'Gunsmith', 'Hideout', 'Bitcoin Farm', 'Bitcoin Farm']
        })
    
    elif item_category == "Keys":
        st.dataframe({
            'Key': ['Marked Room', 'Factory Exit', 'KIBA Store', 'RB-PSP1'],
            'Map': ['Customs', 'Customs/Factory', 'Interchange', 'Reserve'],
            'Value': ['₽80,000', '₽60,000', '₽250,000', '₽180,000']
        })

if __name__ == "__main__":
    main()
