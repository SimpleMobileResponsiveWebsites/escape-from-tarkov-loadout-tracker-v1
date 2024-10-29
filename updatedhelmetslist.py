import streamlit as st
import pandas as pd
from datetime import datetime, time

# Helmet database
HELMETS_DATA = {
    'name': [
        "Shattered lightweight armored mask", "Glorious E lightweight armored mask",
        "Tac-Kek FAST MT helmet (Replica)", "Death Knight mask", "TSh-4M-L soft tank crew helmet",
        "Bomber beanie", "Death Shadow lightweight armored mask", "Jack-o'-lantern tactical pumpkin helmet",
        "Kolpak-1S riot helmet", "ShPM Firefighter helmet", "PSh-97 DJETA riot helmet",
        "LShZ lightweight helmet (Olive Drab)", "6B47 Ratnik-BSh helmet (Olive Drab)",
        "UNTAR helmet", "SSh-68 steel helmet (Olive Drab)", "Galvion Caiman Hybrid helmet (Grey)",
        "FORT Kiver-M bulletproof helmet", "NFM HJELM helmet (Hellhound Grey)",
        "NPP KlASS Tor-2 helmet (Olive Drab)", "SSSh-94 SFERA-S helmet", "DevTac Ronin ballistic helmet",
        "MSA ACH TC-2001 MICH Series helmet", "Ops-Core FAST MT Super High Cut helmet (Black)",
        "Team Wendy EXFIL Ballistic Helmet (Black)", "Altyn bulletproof helmet (Olive Drab)",
        "Vulkan-5 LShZ-5 bulletproof helmet (Black)", "Rys-T bulletproof helmet (Black)"
    ],
    'class': [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5],
    'protected_areas': [
        "Eyes, Face, Jaws, Top", "Eyes, Face, Jaws, Top", "Nape, Top", "Eyes, Top",
        "Ears, Nape, Top", "Nape", "Eyes, Face, Jaws", "All", "Ears, Nape, Top",
        "All", "Ears, Eyes, Face, Nape, Top", "Nape, Top", "Ears, Nape, Top",
        "Ears, Nape, Top", "Ears, Nape, Top", "Nape, Top", "Ears, Nape, Top",
        "Nape, Top", "Ears, Nape, Top", "Ears, Nape, Top", "All", "Nape, Top",
        "Nape, Top", "Nape, Top", "Ears, Nape, Top", "Ears, Nape, Top", "Ears, Nape, Top"
    ],
    'sound_reduction': [
        "None", "None", "None", "None", "Low", "None", "None", "Low", "High",
        "High", "High", "None", "Low", "Low", "None", "None", "High", "None",
        "None", "High", "High", "None", "None", "None", "High", "High", "High"
    ],
    'blocks_headset': [
        "No", "No", "No", "No", "Yes", "No", "No", "Yes", "Yes", "Yes", "Yes",
        "No", "No", "No", "Yes", "No", "Yes", "No", "No", "Yes", "Yes", "No",
        "No", "No", "Yes", "Yes", "Yes"
    ],
    'durability': [
        40, 40, 48, 55, 105, 150, 30, 40, 45, 96, 156, 36, 45, 45, 54, 60, 63,
        78, 81, 135, 180, 30, 48, 54, 81, 75, 90
    ],
    'price': [
        8325, 33895, 23362, 0, 8485, 37113, 57865, 0, 7481, 20042, 9703, 31964,
        39090, 18930, 20424, 62221, 34545, 37619, 58476, 33224, 35245, 44424,
        115301, 137203, 170044, 751688, 156496
    ],
    'trader': [
        "Ragman LL4", "Flea Market", "Flea Market", "N/A", "Flea Market",
        "Flea Market", "Ragman LL4", "N/A", "Flea Market", "Flea Market",
        "Flea Market", "Flea Market", "Prapor LL2", "Ragman LL2", "Flea Market",
        "Peacekeeper LL2", "Ragman LL1", "Flea Market", "Ragman LL3",
        "Flea Market", "Flea Market", "Flea Market", "Peacekeeper LL4",
        "Peacekeeper LL4", "Ragman LL4", "Ragman LL4", "Lavatory 3"
    ]
}

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
        
        # Convert helmet data to DataFrame for easier filtering
        helmets_df = pd.DataFrame(HELMETS_DATA)
        
        # Add filters for helmets
        st.write("Helmet Filters:")
        class_filter = st.multiselect("Armor Class", sorted(list(set(helmets_df['class']))))
        blocks_headset_filter = st.radio("Blocks Headset", ["All", "Yes", "No"])
        max_price = st.slider("Maximum Price (₽)", 
                            min_value=0, 
                            max_value=800000, 
                            value=100000,
                            step=10000)
        
        # Apply filters
        filtered_helmets = helmets_df.copy()
        if class_filter:
            filtered_helmets = filtered_helmets[filtered_helmets['class'].isin(class_filter)]
        if blocks_headset_filter != "All":
            filtered_helmets = filtered_helmets[filtered_helmets['blocks_headset'] == blocks_headset_filter]
        filtered_helmets = filtered_helmets[filtered_helmets['price'] <= max_price]
        
        # Display helmet selection
        selected_helmet = st.selectbox(
            "Helmet",
            ["None"] + list(filtered_helmets['name']),
            format_func=lambda x: x if x == "None" else f"{x} (Class {filtered_helmets[filtered_helmets['name'] == x]['class'].iloc[0]})"
        )
        
        # Display helmet details if one is selected
        if selected_helmet != "None":
            helmet_info = filtered_helmets[filtered_helmets['name'] == selected_helmet].iloc[0]
            st.write("Helmet Details:")
            st.write(f"- Protection: {helmet_info['protected_areas']}")
            st.write(f"- Durability: {helmet_info['durability']}")
            st.write(f"- Sound Reduction: {helmet_info['sound_reduction']}")
            st.write(f"- Price: {helmet_info['price']:,} ₽")
            st.write(f"- Available from: {helmet_info['trader']}")
        
        # Rest of the protection gear
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

    # Rest of the loadout section remains the same...
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

def display_maps_section():
    # Maps section remains the same...
    pass

def display_raid_info():
    # Raid info section remains the same...
    pass

def display_items_database():
    # Items database section remains the same...
    pass

if __name__ == "__main__":
    main()
