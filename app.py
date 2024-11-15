# Update only the relevant CSS section in your code. Replace the freight-cards-container and freight-card CSS with:

        .freight-cards-container {
            display: flex;
            flex-direction: row;
            gap: 1rem;
            padding: 1rem;
            overflow-x: auto;
            width: 100%;
            flex-wrap: nowrap;
            scrollbar-width: thin;
            scrollbar-color: var(--primary-color) transparent;
        }

        .freight-cards-container::-webkit-scrollbar {
            height: 8px;
        }

        .freight-cards-container::-webkit-scrollbar-track {
            background: transparent;
        }

        .freight-cards-container::-webkit-scrollbar-thumb {
            background-color: var(--primary-color);
            border-radius: 4px;
        }

        .freight-card {
            background: linear-gradient(135deg, #000000, #FF0000, #FF69B4);
            border-radius: 10px;
            padding: 1.5rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
            color: #F5F5F5;
            width: 300px;
            height: 300px;
            flex: 0 0 auto;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .freight-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
        }

        .freight-card h3 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: #FFFFFF;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
        }

        .freight-info {
            display: flex;
            align-items: center;
            margin: 0.4rem 0;
        }

        .freight-info-label {
            min-width: 100px;
            color: #FFB6C1;
            font-weight: 500;
        }

        .freight-info-value {
            color: #FFFFFF;
            font-weight: 600;
            text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.3);
        }

# Then update the card HTML structure in the main code to be more compact:
        for _, row in filtered_df.iterrows():
            st.markdown(f"""
                <div class="freight-card">
                    <h3>{row['Destination']}</h3>
                    <div>
                        <div class="freight-info">
                            <span class="freight-info-label">Carrier:</span>
                            <span class="freight-info-value">{row['Carrier']}</span>
                        </div>
                        <div class="freight-info">
                            <span class="freight-info-label">Rate:</span>
                            <span class="freight-info-value">${row['Freight Rate (USD)']}</span>
                        </div>
                        <div class="freight-info">
                            <span class="freight-info-label">Departure:</span>
                            <span class="freight-info-value">{row['Departure Time']}</span>
                        </div>
                        <div class="freight-info">
                            <span class="freight-info-label">Transit:</span>
                            <span class="freight-info-value">{row['Transit Time (Hours)']}h</span>
                        </div>
                        <div class="freight-info">
                            <span class="freight-info-label">Type:</span>
                            <span class="freight-info-value">{row['Freight Type']}</span>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
