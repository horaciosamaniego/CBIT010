# %% [markdown]
# # 🌿 Semana 12 · Laboratorio: Pandas avanzado + Visualización
#
# **Del dato al gráfico ecológico**
#
# ---
# Archivo → Guardar una copia en Drive.

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from google.colab import drive

drive.mount('/content/drive')

# Cargar datasets (ajusta rutas)
ruta_base = "/content/drive/MyDrive/CBIT010_Archivos_ayudantia/"
df = pd.read_csv(ruta_base + "Semana11/bosque_valdiviano_simple.csv")
cam = pd.read_csv(ruta_base + "Semana11/camaras_trampa_simulado.csv")

print(f"✅ Bosque: {df.shape[0]} filas | Cámaras: {cam.shape[0]} filas")

# %%
# Funciones de diversidad (reutilizables)
def shannon_entropy(abundancias):
    total = sum(abundancias)
    H = 0
    for n in abundancias:
        if n > 0:
            p = n / total
            H -= p * math.log(p)
    return H

def equitatividad(abundancias):
    S = len(abundancias)
    if S <= 1: return 0.0
    return shannon_entropy(abundancias) / math.log(S)

# %% [markdown]
# ---
# ## Ejercicio 1: Exploración visual del bosque 📊

# %%
# 1a. Gráfico de barras — abundancia por especie
conteos = df["especie"].value_counts()

fig, ax = plt.subplots(figsize=(10, 5))
conteos.plot(kind="bar", ax=ax, color="#2E7D32", edgecolor="white")
ax.set_title("Abundancia por especie — Bosque Valdiviano", fontsize=14)
ax.set_ylabel("Nº de individuos")
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.show()

# %%
# 1b. Histograma de DAP con línea de media
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(df["dap_cm"], bins=15, color="#00796B", edgecolor="white", alpha=0.8)
ax.axvline(df["dap_cm"].mean(), color="red", linestyle="--",
           label=f"Media: {df['dap_cm'].mean():.1f} cm")
ax.set_xlabel("DAP (cm)")
ax.set_ylabel("Frecuencia")
ax.set_title("Distribución de DAP")
ax.legend()
plt.tight_layout()
plt.show()

# %%
# 1c. Boxplot de DAP por especie
# TU CÓDIGO AQUÍ
fig, ax = plt.subplots(figsize=(10, 5))
df.boxplot(column="dap_cm", by="especie", ax=ax, rot=45)
ax.set_title("DAP por especie")
ax.set_ylabel("DAP (cm)")
plt.suptitle("")   # quitar título automático de pandas
plt.tight_layout()
plt.show()

# %% [markdown]
# ---
# ## Ejercicio 2: Relaciones DAP-Altura 🔬

# %%
# 2a. Scatter DAP vs Altura coloreado por especie
fig, ax = plt.subplots(figsize=(9, 6))

for especie, grupo in df.groupby("especie"):
    ax.scatter(grupo["dap_cm"], grupo["altura_m"],
               label=especie, alpha=0.7, s=50)

ax.set_xlabel("DAP (cm)", fontsize=12)
ax.set_ylabel("Altura (m)", fontsize=12)
ax.set_title("Relación DAP-Altura por especie", fontsize=14)
ax.legend(fontsize=9, loc="lower right")
plt.tight_layout()
plt.show()

# %%
# 2b. TU CÓDIGO AQUÍ — Scatter DAP vs Altura coloreado por PARCELA
fig, ax = plt.subplots(figsize=(9, 6))

for parcela, grupo in df.groupby("parcela"):
    ax.scatter(grupo["dap_cm"], grupo["altura_m"],
               label=f"Parcela {parcela}", alpha=0.7, s=50)

ax.set_xlabel("DAP (cm)")
ax.set_ylabel("Altura (m)")
ax.set_title("Relación DAP-Altura por parcela")
ax.legend()
plt.tight_layout()
plt.show()

# %% [markdown]
# **Pregunta:** ¿Se observan diferencias en la relación DAP-Altura entre especies? ¿Y entre parcelas?

# %% [markdown]
# ---
# ## Ejercicio 3: Diversidad visual por parcela 🌿

# %%
# 3a. Calcular H' y J por parcela
resultados = []
for parcela, grupo in df.groupby("parcela"):
    conteos = grupo["especie"].value_counts()
    H = shannon_entropy(conteos.values)
    J = equitatividad(conteos.values)
    S = len(conteos)
    N = len(grupo)
    resultados.append({"parcela": parcela, "S": S, "N": N, "H": H, "J": J})

div = pd.DataFrame(resultados)
print(div.round(4))

# %%
# 3b. Gráfico de barras de H' por parcela
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(div["parcela"].astype(str), div["H"], color="#1565C0", edgecolor="white")
ax.set_xlabel("Parcela")
ax.set_ylabel("Shannon H' (nats)")
ax.set_title("Diversidad por parcela")

# Agregar valores encima de las barras
for i, row in div.iterrows():
    ax.text(i, row["H"] + 0.02, f"{row['H']:.3f}", ha="center", fontsize=10,
            color="white")

plt.tight_layout()
plt.show()

# %%
# 3c. TU CÓDIGO AQUÍ — Gráfico de barras de N (abundancia) por parcela
# ¿La parcela con más individuos es la más diversa?
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(div["parcela"].astype(str), div[___], color="#F57F17", edgecolor="white")
ax.set_xlabel("Parcela")
ax.set_ylabel("Nº de individuos")
ax.set_title("Abundancia total por parcela")
plt.tight_layout()
plt.show()

# %% [markdown]
# **Pregunta:** ¿La parcela con más individuos es la más diversa? ¿Qué papel juega la equitatividad (J)?

# %% [markdown]
# ---
# ## Ejercicio 4: Cámaras trampa — análisis temporal 📅

# %%
# 4a. Convertir fecha y extraer mes
cam["fecha"] = pd.to_datetime(cam["fecha"])
cam["mes"] = cam["fecha"].dt.month

# Registros por mes
fig, ax = plt.subplots(figsize=(8, 5))
cam["mes"].value_counts().sort_index().plot(kind="bar", ax=ax, color="#00897B")
ax.set_xlabel("Mes")
ax.set_ylabel("Nº registros")
ax.set_title("Registros por mes — Cámaras trampa")
plt.tight_layout()
plt.show()

# %%
# 4b. Registros por sitio, coloreado por método
tabla_metodo = cam.groupby(["sitio", "metodo"]).size().unstack(fill_value=0)

fig, ax = plt.subplots(figsize=(10, 5))
tabla_metodo.plot(kind="bar", ax=ax, edgecolor="white")
ax.set_ylabel("Nº registros")
ax.set_title("Registros por sitio y método de muestreo")
ax.tick_params(axis='x', rotation=0)
ax.legend(title="Método")
plt.tight_layout()
plt.show()

# %%
# 4c. Curva rango-abundancia por sitio (4 subplots)
sitios = cam["sitio"].unique()

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for i, sitio in enumerate(sorted(sitios)):
    datos_sitio = cam[cam["sitio"] == sitio]
    conteos = datos_sitio["especie"].value_counts()
    
    axes[i].bar(range(len(conteos)), conteos.values, color="#1565C0", edgecolor="white")
    axes[i].set_xticks(range(len(conteos)))
    axes[i].set_xticklabels(conteos.index, rotation=45, ha="right", fontsize=8)
    axes[i].set_title(sitio, fontsize=12)
    axes[i].set_ylabel("Registros")

plt.suptitle("Curvas rango-abundancia por sitio", fontsize=14, y=1.01)
plt.tight_layout()
plt.show()

# %% [markdown]
# **Pregunta:** ¿Cuál sitio tiene la curva más plana (más equitativa)? ¿Cuál la más empinada?

# %% [markdown]
# ---
# ## 🏆 Ejercicio 5 (Desafío): Figura de calidad de publicación
#
# Crea una figura con **4 subplots** que resuma el dataset forestal:
# 1. Curva rango-abundancia
# 2. Distribución de DAP (histograma)
# 3. Relación DAP-Altura (scatter por especie)
# 4. Diversidad H' por parcela (barras)
#
# Requisitos: título general, ejes etiquetados, leyenda donde corresponda.
# Guardar como PDF y PNG.

# %%
# TU CÓDIGO AQUÍ
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: rango-abundancia
conteos = df["especie"].value_counts()
axes[0, 0].bar(range(len(conteos)), conteos.values, color="#2E7D32", edgecolor="white")
axes[0, 0].set_xticks(range(len(conteos)))
axes[0, 0].set_xticklabels(conteos.index, rotation=45, ha="right", fontsize=9)
axes[0, 0].set_title("a) Rango-abundancia")
axes[0, 0].set_ylabel("Abundancia")

# Panel 2: histograma DAP
axes[0, 1].hist(df["dap_cm"], bins=15, color="#00796B", edgecolor="white")
axes[0, 1].axvline(df["dap_cm"].mean(), color="red", linestyle="--")
axes[0, 1].set_title("b) Distribución de DAP")
axes[0, 1].set_xlabel("DAP (cm)")
axes[0, 1].set_ylabel("Frecuencia")

# Panel 3: scatter DAP vs Altura
for especie, grupo in df.groupby("especie"):
    axes[1, 0].scatter(grupo["dap_cm"], grupo["altura_m"],
                        label=especie, alpha=0.6, s=40)
axes[1, 0].set_title("c) Relación DAP-Altura")
axes[1, 0].set_xlabel("DAP (cm)")
axes[1, 0].set_ylabel("Altura (m)")
axes[1, 0].legend(fontsize=7, loc="lower right")

# Panel 4: H' por parcela
axes[1, 1].bar(div["parcela"].astype(str), div["H"], color="#1565C0", edgecolor="white")
axes[1, 1].set_title("d) Shannon H' por parcela")
axes[1, 1].set_xlabel("Parcela")
axes[1, 1].set_ylabel("H' (nats)")

plt.suptitle("Inventario forestal — Bosque Valdiviano", fontsize=16, y=1.01)
plt.tight_layout()

# Guardar
fig.savefig("resumen_bosque_valdiviano.pdf", bbox_inches="tight")
fig.savefig("resumen_bosque_valdiviano.png", dpi=150, bbox_inches="tight")
print("✅ Figura guardada como PDF y PNG")
plt.show()

# %% [markdown]
# ---
# ## 🏁 Fin del laboratorio
#
# **Checklist:**
# - [ ] ¿Los gráficos del Ej. 1 se ven correctos?
# - [ ] ¿El scatter DAP-Altura muestra diferencias entre especies?
# - [ ] ¿H' varía entre parcelas?
# - [ ] ¿Las curvas rango-abundancia difieren entre sitios?
# - [ ] (Desafío) ¿La figura de 4 paneles se guardó como PDF?
#
# **A continuación:** Quiz 5 (15 min)
#
# ---
# *Semana 12 · Pandas avanzado + Visualización · UACh 2026*
