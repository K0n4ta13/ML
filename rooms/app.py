import streamlit as st
from util import (
    get_tenant_ids,
    generate_compatibility_chart,
    generate_compatibility_table,
)
from logic import compatible_tenants


def main():
    st.set_page_config(layout="wide")
    st.image("./assets/cover.png", use_container_width=True)
    st.markdown('<div style="margin-top: 60px;"></div>', unsafe_allow_html=True)

    result = None

    with st.sidebar:
        st.header("Who is already leaving in the apartment?")
        tenant1 = st.text_input("Tenant 1")
        tenant2 = st.text_input("Tenant 2")
        tenant3 = st.text_input("Tenant 3")

        housemates = st.text_input("How many housemates do you want to look for?")

        if st.button("Search housemates"):
            try:
                top_housemates = int(housemates)
            except ValueError:
                st.error("Please enter a valid number.")
                top_housemates = None

            tenant_ids = get_tenant_ids(tenant1, tenant2, tenant3)

            if tenant_ids and top_housemates is not None:
                result = compatible_tenants(tenant_ids, top_housemates)

    if isinstance(result, str):
        st.error(result)
    elif result is not None:
        cols = st.columns((1, 2))

        with cols[0]:
            st.write("Compatibility level of each new housemate:")
            fig_grafico = generate_compatibility_chart(result[1])
            st.pyplot(fig_grafico)

        with cols[1]:
            st.write("Comparison between housemates:")
            fig_tabla = generate_compatibility_table(result)
            st.plotly_chart(fig_tabla, use_container_width=True)


if __name__ == "__main__":
    main()
