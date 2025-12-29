"""
v3.6: EU AI Act & NIST Compliance Checker
Validates compliance with EU AI Act and NIST IR 8312.

Author: Nazlı Özgür
Date: December 2025
"""
import json
from datetime import datetime


class GovernanceAuditor:
    """Audit ML system for regulatory compliance."""
    
    def __init__(self):
        self.audit_results = {}
    
    def check_data_quality(self, data_quality_score, threshold=80):
        """EU AI Act Article 10: Data Quality."""
        compliant = data_quality_score >= threshold
        
        result = {
            'article': 'EU AI Act Article 10',
            'requirement': 'Data Quality',
            'score': data_quality_score,
            'threshold': threshold,
            'compliant': compliant,
            'checked_at': datetime.now().isoformat()
        }
        
        self.audit_results['data_quality'] = result
        print(f"{'✅' if compliant else '❌'} Data Quality: {data_quality_score:.1f}/100")
        
        return result
    
    def check_fairness(self, fairness_ratio, threshold=0.80):
        """EU AI Act Article 10: Non-discrimination."""
        compliant = fairness_ratio >= threshold
        
        result = {
            'article': 'EU AI Act Article 10',
            'requirement': 'Non-Discrimination',
            'fairness_ratio': fairness_ratio,
            'threshold': threshold,
            'compliant': compliant,
            'checked_at': datetime.now().isoformat()
        }
        
        self.audit_results['fairness'] = result
        print(f"{'✅' if compliant else '❌'} Fairness: {fairness_ratio:.3f}")
        
        return result
    
    def check_nist_explainability(self, fidelity_score, threshold=0.90):
        """NIST Principle 1: Explanation."""
        compliant = fidelity_score >= threshold
        
        result = {
            'standard': 'NIST IR 8312 Principle 1',
            'requirement': 'Explanation',
            'fidelity_score': fidelity_score,
            'threshold': threshold,
            'compliant': compliant,
            'checked_at': datetime.now().isoformat()
        }
        
        self.audit_results['nist_explainability'] = result
        print(f"{'✅' if compliant else '❌'} NIST Explainability: {fidelity_score:.3f}")
        
        return result
    
    def generate_audit_report(self, filepath='docs/compliance_audit.json'):
        """Generate compliance audit report."""
        from pathlib import Path
        
        total_checks = len(self.audit_results)
        passed_checks = sum(1 for r in self.audit_results.values() if r['compliant'])
        compliance_rate = (passed_checks / total_checks * 100) if total_checks > 0 else 0
        
        report = {
            'generated_at': datetime.now().isoformat(),
            'overall_compliance': compliance_rate,
            'total_checks': total_checks,
            'passed_checks': passed_checks,
            'failed_checks': total_checks - passed_checks,
            'details': self.audit_results
        }
        
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n{'='*60}")
        print(f"COMPLIANCE AUDIT SUMMARY")
        print(f"{'='*60}")
        print(f"Overall Compliance: {compliance_rate:.1f}%")
        print(f"Passed: {passed_checks}/{total_checks}")
        print(f"Report saved: {filepath}")
        print(f"{'='*60}")
        
        return report


if __name__ == "__main__":
    print("Governance Auditor Ready!")
    print("Checks: EU AI Act + NIST IR 8312")
