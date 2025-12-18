import streamlit as st
import requests

st.set_page_config(page_title="SHL Assessment Recommender")

st.title("SHL Assessment Recommendation System")

query = st.text_area(
    "Enter hiring requirement or job description",
    placeholder="e.g. Looking to hire mid-level professionals proficient in Python, SQL, and JavaScript"
)

top_k = st.number_input("Number of recommendations", min_value=1, max_value=10, value=10)

if st.button("Recommend Assessments"):
    if not query.strip():
        st.warning("Please enter a hiring query.")
    else:
        with st.spinner("Generating recommendations..."):
            try:
                response = requests.post(
                    "http://localhost:8000/recommend",
                    json={"query": query, "k": top_k},
                    timeout=30
                )

                response.raise_for_status()
                results = response.json()

                if not results:
                    st.info("No recommendations found.")
                else:
                    st.success("Recommended Assessments")
                    for r in results:
                        st.markdown(f"### {r['assessment_name']}")
                        st.write(f"**Test Type:** {r['test_type']}")
                        st.write(r.get("reason", ""))
                        st.markdown(f"[View Assessment]({r['url']})")
                        st.divider()

            except Exception as e:
                st.error(f"Backend error: {e}")
