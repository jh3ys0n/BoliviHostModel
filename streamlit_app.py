import pandas as pd
import streamlit as st
import pickle

def preprocess_data(df):
    # Convertir variables categóricas a one-hot encoding
    return df

def check_and_update_key(data, key_prefix, value):
    for key in data:
        if key == key_prefix + value:
            data[key] = 1  # Asigna el nuevo valor si se cumple la condición

def user_input_parameters():
    meses_activo = st.sidebar.slider("Antigüedad en meses", 0, 73, 2)

    total = st.sidebar.slider("Precio del servicio", 0, 2000, 99)

    # Selección adicional de opciones:
    state = st.sidebar.selectbox("Ciudad", ["Beni", "Chuquisaca", "Cochabamba", "La Paz", "Oruro", "Potosí", "Santa Cruz", "Tarija"])
    paymentmethod = st.sidebar.selectbox("Método de pago", ["banktransfer", "paypal", "qr", "walletbo"])
    billingcycle = st.sidebar.selectbox("Frecuencia de pago", ["Annually", "Biennially", "Free Account", "Monthly", "One Time", "Quarterly", "Semi-Annually", "Triennially"])
    nombre_servicio = st.sidebar.selectbox("Servicio", [
        'cloud_plus', 'cloud_x1', 'jupiter_shared_x1', 'shared_turbo_xxl', 'cloud_x3', 'shared_turbo_l', 'cloud_x2', 'audio_pro', 'vps_plus', 'streaming_basic', 'shared_turbo_xl', 'audio_plus', 'streaming_pro', 'desarrollo_web_basic', 'moodle_xl', 'correo_xl', 'hosting_plus_promocion_16_de_julio', 'cloud_x5', 'cloud_basic', 'audio_dealer', 'netflix_cuenta_compartida', 'correo_l', 'jupiter_vip_shared_hosting_pro', 'moodle_xxl', 'moodle_l', 'cloud_x10', 'eset_nod32_antivirus_2018_v11_1_usuario', 'web_developer_en_7_dias', 'shared_x1', 'streaming_plus', 'plus', 'black_friday', 'whats_xl', 'whats_xxl', 'hola2018', 'cloud_8x_legacy', 'wordpress_xl', 'desarrollo_web_plus', 'elearning_pro', 'wordpress_l', 'vps_one', 'llajwa_hosting_plus', 'shared_x2', 'vps_micro', 'jupiter_shared_x3', 'moodle_x1', 'lite_free', 'odoo_plus', 'vps_0', 'correo_xxl', 'lite_plus', 'video_xxxl', 'windows_xxl', 'venus_vip_shared_hosting_plus', 'windows_xl', 'combo_play', 'video_l', 'video_xl', 'enterprise_plus', 'windows_l', 'vps_1', 'unlimited', 'privado_xl', 'cms_l', 'enterprise_one', 'correo_xxl_300', 'plantilla_wordpress_themeforest', 'windows_vps_l', 'black_sheep_cloud', 'moodle_x3', 'whats_l', 'windows_vps_xxl', 'wordpress_en_shared_hosting', 'zoom_pro', 'moodle_x2', 'cloud_plus', 'privado_l', 'vps_power', 'reseller_basic', 'vps_ovz_micro', 'dedicado_l', 'correo_corporativo_cpanel', 'storage_250gb', 'video_xxl', 'constructor_l', 'comodo_positivessl', 'digitalizate_o_muere'
    ])

    data = {
        "meses_activo": meses_activo,
        "total": total,
        "nombre_servicio_audio_dealer": 0,
        "nombre_servicio_audio_plus": 0,
        "nombre_servicio_audio_pro": 0,
        "nombre_servicio_black_friday": 0,
        "nombre_servicio_black_sheep_cloud": 0,
        "nombre_servicio_cloud_8x_legacy": 0,
        "nombre_servicio_cloud_basic": 0,
        "nombre_servicio_cloud_plus": 0,
        "nombre_servicio_cloud_x1": 0,
        "nombre_servicio_cloud_x10": 0,
        "nombre_servicio_cloud_x2": 0,
        "nombre_servicio_cloud_x3": 0,
        "nombre_servicio_cloud_x5": 0,
        "nombre_servicio_cms_l": 0,
        "nombre_servicio_combo_play": 1,
        "nombre_servicio_comodo_positivessl": 0,
        "nombre_servicio_constructor_l": 0,
        "nombre_servicio_correo_corporativo_cpanel": 0,
        "nombre_servicio_correo_l": 0,
        "nombre_servicio_correo_xl": 0,
        "nombre_servicio_correo_xxl": 0,
        "nombre_servicio_correo_xxl_300": 0,
        "nombre_servicio_dedicado_l": 0,
        "nombre_servicio_desarrollo_web_basic": 0,
        "nombre_servicio_desarrollo_web_plus": 0,
        "nombre_servicio_digitalizate_o_muere": 0,
        "nombre_servicio_elearning_pro": 0,
        "nombre_servicio_enterprise_one": 0,
        "nombre_servicio_enterprise_plus": 0,
        "nombre_servicio_eset_nod32_antivirus_2018_v11_1_usuario": 0,
        "nombre_servicio_hola2018": 0,
        "nombre_servicio_hosting_plus_promocion_16_de_julio": 0,
        "nombre_servicio_jupiter_shared_x1": 0,
        "nombre_servicio_jupiter_shared_x3": 0,
        "nombre_servicio_jupiter_vip_shared_hosting_pro": 0,
        "nombre_servicio_lite_free": 0,
        "nombre_servicio_lite_plus": 0,
        "nombre_servicio_llajwa_hosting_plus": 0,
        "nombre_servicio_moodle_l": 0,
        "nombre_servicio_moodle_x1": 0,
        "nombre_servicio_moodle_x2": 0,
        "nombre_servicio_moodle_x3": 0,
        "nombre_servicio_moodle_xl": 0,
        "nombre_servicio_moodle_xxl": 0,
        "nombre_servicio_netflix_cuenta_compartida": 0,
        "nombre_servicio_odoo_plus": 0,
        "nombre_servicio_plantilla_wordpress_themeforest": 0,
        "nombre_servicio_plus": 0,
        "nombre_servicio_privado_l": 0,
        "nombre_servicio_privado_xl": 0,
        "nombre_servicio_reseller_basic": 0,
        "nombre_servicio_shared_turbo_l": 0,
        "nombre_servicio_shared_turbo_xl": 0,
        "nombre_servicio_shared_turbo_xxl": 0,
        "nombre_servicio_shared_x1": 0,
        "nombre_servicio_shared_x2": 0,
        "nombre_servicio_storage_250gb": 0,
        "nombre_servicio_streaming_basic": 0,
        "nombre_servicio_streaming_plus": 0,
        "nombre_servicio_streaming_pro": 0,
        "nombre_servicio_unlimited": 0,
        "nombre_servicio_venus_vip_shared_hosting_plus": 0,
        "nombre_servicio_video_l": 0,
        "nombre_servicio_video_xl": 0,
        "nombre_servicio_video_xxl": 0,
        "nombre_servicio_video_xxxl": 0,
        "nombre_servicio_vps_0": 0,
        "nombre_servicio_vps_1": 0,
        "nombre_servicio_vps_micro": 0,
        "nombre_servicio_vps_one": 0,
        "nombre_servicio_vps_ovz_micro": 0,
        "nombre_servicio_vps_plus": 0,
        "nombre_servicio_vps_power": 0,
        "nombre_servicio_web_developer_en_7_dias": 0,
        "nombre_servicio_whats_l": 0,
        "nombre_servicio_whats_xl": 0,
        "nombre_servicio_whats_xxl": 0,
        "nombre_servicio_windows_l": 0,
        "nombre_servicio_windows_vps_l": 0,
        "nombre_servicio_windows_vps_xxl": 0,
        "nombre_servicio_windows_xl": 0,
        "nombre_servicio_windows_xxl": 0,
        "nombre_servicio_wordpress_en_shared_hosting": 0,
        "nombre_servicio_wordpress_l": 0,
        "nombre_servicio_wordpress_xl": 0,
        "nombre_servicio_zoom_pro": 0,
        "paymentmethod_banktransfer": 0,
        "paymentmethod_paypal": 0,
        "paymentmethod_qr": 0,
        "paymentmethod_walletbo": 0,
        "billingcycle_Annually": 1,
        "billingcycle_Biennially": 0,
        "billingcycle_Free Account": 0,
        "billingcycle_Monthly": 0,
        "billingcycle_One Time": 0,
        "billingcycle_Quarterly": 0,
        "billingcycle_Semi-Annually": 0,
        "billingcycle_Triennially": 0,
        "state_Beni": 0,
        "state_Chuquisaca": 0,
        "state_Cochabamba": 0,
        "state_La Paz": 0,
        "state_Oruro": 0,
        "state_Pando": 0,
        "state_Potosí": 0,
        "state_Santa Cruz": 0,
        "state_Tarija": 0
    }

    check_and_update_key(data, "state_", state)
    check_and_update_key(data, "billingcycle_", billingcycle)
    check_and_update_key(data, "paymentmethod_", paymentmethod)
    check_and_update_key(data, "nombre_servicio_", nombre_servicio)

    # Convertir el diccionario a DataFrame
    df = pd.DataFrame(data, index=[0])

    return df

def classify(num):
    if num == "Activo":
        return "Activo"
    elif num == "Cancelado":
        return "Cancelado"
    elif num == "Pendiente":
        return "Pendiente"
    elif num == "Suspendido":
        return "Suspendido"
    else:
        return "Terminado"

def main():
    st.title("Modelamiento predicito para el abandono de clientes en una empresa de alojamiento web")

    st.sidebar.header("Parámetros de entrada del usuario")

    df = user_input_parameters()

    option = ['regresion logistica']

    model_type = st.sidebar.selectbox('¿Qué modelo te gustaría usar?', option)

    st.subheader(f'Parámetros de entrada del usuario - Modelo seleccionado: {model_type}')
    st.write(df)
    with open('best_decision_tree.pkl', 'rb') as rl:
        model = pickle.load(rl)

        if hasattr(model, 'estimators_'):
            st.success("¡El modelo RandomForest está cargado y ajustado!")

    if st.button('EJECUTAR'):
        # Preprocesamiento y codificación one-hot
        df_processed = preprocess_data(df)
        # Predicción
        prediction = model.predict(df_processed)
        # Clasificación de la predicción
        classification = classify(prediction)

        st.success(f"Predicción: {prediction}")

if __name__ == '__main__':
    main()
