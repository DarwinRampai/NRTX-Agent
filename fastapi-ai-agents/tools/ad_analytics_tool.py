class AdAnalyticsTool:
    def __init__(self):
        self.analytics_data = {}

    def log_ad_performance(self, ad_id, performance_metrics):
        self.analytics_data[ad_id] = performance_metrics

    def get_ad_performance(self, ad_id):
        return self.analytics_data.get(ad_id, "No data available for this ad.")

    def generate_report(self):
        report = "Ad Performance Report:\n"
        for ad_id, metrics in self.analytics_data.items():
            report += f"Ad ID: {ad_id}, Metrics: {metrics}\n"
        return report.strip()