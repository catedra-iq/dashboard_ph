import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from pHcalc.pHcalc import Acid, Neutral, System 

st.markdown(
        """
        Holi, nada que ver por aqui
        """
)


na_moles = np.linspace(1e-8, 5.e-3, 500)
sol_volume = 1. # Liter
phos = Acid(pKa=[2.148, 7.198, 12.375], charge=0, conc=1.e-3)
phs = []
for mol in na_moles:
    na = Neutral(charge=1, conc=mol/sol_volume)
    system = System(phos, na)
    system.pHsolve(guess_est=True)
    phs.append(system.pH)
plt.plot(na_moles, phs)
st.pyplot(plt.gcf())
plt.show()


phos = Acid(pKa=[2.148, 7.198, 12.319], charge=0, conc=0.01)
phs = np.linspace(0, 14, 1000)
fracs = phos.alpha(phs)
plt.plot(phs, fracs)
st.pyplot(plt.gcf())
plt.show()
