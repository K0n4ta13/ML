import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("dataset_tenants.csv", index_col="id_inquilino")

df.columns = [
    "horario",
    "bioritmo",
    "nivel_educativo",
    "leer",
    "animacion",
    "cine",
    "mascotas",
    "cocinar",
    "deporte",
    "dieta",
    "fumador",
    "visitas",
    "orden",
    "musica_tipo",
    "musica_alta",
    "plan_perfecto",
    "instrumento",
]

enc = OneHotEncoder(sparse_output=False)
encoded_df = enc.fit_transform(df)

encoded_feature_names = enc.get_feature_names_out()

matrix_s = np.dot(encoded_df, encoded_df.T)

min_range = -100
max_range = 100

min_original = np.min(matrix_s)
max_original = np.max(matrix_s)

scaled_matrix_s = ((matrix_s - min_original) / (max_original - min_original)) * (
    max_range - min_range
) + min_range

df_s = pd.DataFrame(scaled_matrix_s, index=df.index, columns=df.index)


def compatible_tenants(tenant_ids, top_housemates):
    for tenant_id in tenant_ids:
        if tenant_id not in df_s.index:
            return "At least one tenant not found"

    tenant_rows = df_s.loc[tenant_ids]
    average_similarity = tenant_rows.mean(axis=0)
    similar_tenants = average_similarity.sort_values(ascending=False)
    similar_tenants = similar_tenants.drop(tenant_ids)
    top_housemates_similar_tenants = similar_tenants.head(top_housemates)
    similar_records = df.loc[top_housemates_similar_tenants.index]
    searched_records = df.loc[tenant_ids]
    result = pd.concat([searched_records.T, similar_records.T], axis=1)
    similarity_series = pd.Series(
        data=top_housemates_similar_tenants.values,
        index=top_housemates_similar_tenants.index,
        name="Similarity",
    )

    return (result, similarity_series)
