import streamlit as st
import numpy as np

weights=np.array([ 0.02192892,  0.13802519,  0.07824501,  0.08748403,  0.01061873,
        0.07854782,  0.03234228, -0.06459426,  0.10739289,  0.07638642,
        0.18675382])
C=11.16844925783286

def f(LotArea, FirstFlrSF, SecondFlrSF, TotalBsmtSF, BsmtFinSF2, BsmtFinSF1, BsmtUnfSF, BedroomAbvGr, BsmtFullBath, BsmtHalfBath, FullBath):
    inp=np.array([LotArea,FirstFlrSF,SecondFlrSF,TotalBsmtSF,BsmtFinSF2,BsmtFinSF1,BsmtUnfSF,BedroomAbvGr,
              BsmtFullBath,BsmtHalfBath,FullBath])
    return np.exp(sum(weights*inp)+C)

st.title('Predict prices here')

# Input features
LotArea = st.number_input('LotArea')
FirstFlrSF = st.number_input('1stFlrSF')
SecondFlrSF = st.number_input('2ndFlrSF')
TotalBsmtSF = st.number_input('TotalBsmtSF')
BsmtFinSF2 = st.number_input('BsmtFinSF2')
BsmtFinSF1 = st.number_input('BsmtFinSF1')
BsmtUnfSF = st.number_input('BsmtUnfSF')
BedroomAbvGr = st.number_input('BedroomAbvGr')
BsmtFullBath = st.number_input('BsmtFullBath')
BsmtHalfBath = st.number_input('BsmtHalfBath')
FullBath = st.number_input('FullBath')



# Calculate output
output = f(LotArea, FirstFlrSF, SecondFlrSF, TotalBsmtSF, BsmtFinSF2, BsmtFinSF1, BsmtUnfSF, BedroomAbvGr, BsmtFullBath, BsmtHalfBath, FullBath)

# Display output
st.write('Estimated price: ', f'₹ {round(output,2)}')