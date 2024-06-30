# react-streamlit
prototype to display GoodData React Components inside a Streamlit application

## Streamlit application

- acts as a main wrapper
- `gooddata_component` contains the React application (below)

```
python -m venv venv
source venv/bin/activate
pip install -r ./requirements.txt
```

## React application

```
# yarn create react-app gooddata-react --template typescript
npx @gooddata/app-toolkit@latest init
cd gooddata-react
yarn add streamlit-component-lib
yarn start
```

