#!/usr/bin/env python3
"""
BMAD Skills Activation Metrics System
Tracks and analyzes skill activation patterns for optimization
"""

import yaml
from datetime import datetime
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Optional


class ActivationMetrics:
    """Manages activation metrics collection and analysis"""

    def __init__(self, metrics_file='docs/activation-metrics.yaml'):
        self.metrics_file = Path(metrics_file)
        self.metrics_file.parent.mkdir(parents=True, exist_ok=True)

    def log_activation(
        self,
        skill_name: str,
        trigger_phrase: str,
        confidence: float,
        context: Optional[Dict] = None,
        success: bool = True,
        notes: str = ""
    ):
        """
        Log a skill activation event

        Args:
            skill_name: Name of activated skill
            trigger_phrase: Phrase that triggered activation
            confidence: Confidence score (0-1)
            context: Additional context (phase, artifacts, etc.)
            success: Whether activation was successful
            notes: Additional notes or error messages
        """
        confidence_value = self._validate_activation_input(
            skill_name,
            trigger_phrase,
            confidence,
            context,
        )

        metrics = self._load_metrics()

        activation = {
            'timestamp': datetime.now().isoformat(),
            'skill': skill_name,
            'trigger': trigger_phrase,
            'confidence': confidence_value,
            'context': context or {},
            'success': success,
            'notes': notes
        }

        metrics['activations'].append(activation)
        metrics['summary']['total_activations'] += 1
        metrics['summary']['by_skill'][skill_name] = \
            metrics['summary']['by_skill'].get(skill_name, 0) + 1

        if success:
            metrics['summary']['successful_activations'] += 1
        else:
            metrics['summary']['failed_activations'] += 1

        self._save_metrics(metrics)

    def get_stats(self) -> Dict:
        """Get activation statistics"""
        metrics = self._load_metrics()
        activations = metrics['activations']

        if not activations:
            return {
                'total': 0,
                'success_rate': 0,
                'by_skill': {},
                'common_triggers': [],
                'avg_confidence': 0
            }

        # Calculate stats
        total = len(activations)
        successful = sum(1 for a in activations if a['success'])
        success_rate = (successful / total * 100) if total > 0 else 0

        # By skill
        by_skill = Counter(a['skill'] for a in activations)

        # Common triggers
        trigger_counter = Counter(a['trigger'] for a in activations)
        common_triggers = trigger_counter.most_common(10)

        # Average confidence
        confidences = [a['confidence'] for a in activations if 'confidence' in a]
        avg_confidence = sum(confidences) / len(confidences) if confidences else 0

        # Low confidence activations (may need improvement)
        low_confidence = [
            {
                'skill': a['skill'],
                'trigger': a['trigger'],
                'confidence': a['confidence']
            }
            for a in activations
            if a.get('confidence', 1.0) < 0.7
        ]

        return {
            'total': total,
            'successful': successful,
            'failed': total - successful,
            'success_rate': round(success_rate, 2),
            'by_skill': dict(by_skill),
            'common_triggers': common_triggers,
            'avg_confidence': round(avg_confidence, 2),
            'low_confidence_activations': low_confidence[:5]
        }

    def analyze_patterns(self) -> Dict:
        """Analyze activation patterns for insights"""
        metrics = self._load_metrics()
        activations = metrics['activations']

        if not activations:
            return {'insights': [], 'recommendations': []}

        insights = []
        recommendations = []

        # Analyze skill distribution
        skill_counts = Counter(a['skill'] for a in activations)
        total = len(activations)

        # Underutilized skills
        for skill in ['bmad-analyst', 'bmad-pm', 'bmad-architecture', 'bmad-dev',
                     'openspec-propose', 'openspec-implement', 'openspec-archive']:
            count = skill_counts.get(skill, 0)
            percentage = (count / total * 100) if total > 0 else 0

            if percentage < 5 and total > 20:
                insights.append(f"{skill} is underutilized ({percentage:.1f}%)")
                recommendations.append(
                    f"Consider adding more trigger phrases for {skill}"
                )

        # Failed activations analysis
        failed = [a for a in activations if not a['success']]
        if failed:
            failed_skills = Counter(a['skill'] for a in failed)
            for skill, count in failed_skills.most_common(3):
                insights.append(f"{skill} has {count} failed activations")
                recommendations.append(
                    f"Review {skill} prerequisites and error handling"
                )

        # Routing patterns
        orchestrator_count = skill_counts.get('bmad-orchestrator', 0)
        if orchestrator_count > total * 0.5:
            insights.append(
                "High orchestrator usage - good workflow coordination"
            )
        elif orchestrator_count < total * 0.1 and total > 10:
            insights.append("Low orchestrator usage - may indicate direct skill calls")
            recommendations.append(
                "Ensure users start with 'what's next' or status checks"
            )

        # OpenSpec vs BMAD balance
        openspec_count = sum(
            skill_counts.get(s, 0)
            for s in ['openspec-propose', 'openspec-implement', 'openspec-archive']
        )
        bmad_count = total - openspec_count

        if total > 10:
            openspec_pct = (openspec_count / total * 100)
            insights.append(
                f"Workflow split: {openspec_pct:.1f}% OpenSpec, "
                f"{100-openspec_pct:.1f}% BMAD"
            )

            if openspec_pct > 80:
                insights.append("Mostly lightweight changes - good for iterations")
            elif openspec_pct < 20:
                insights.append("Mostly complex work - good for new features")

        return {
            'insights': insights,
            'recommendations': recommendations
        }

    def view_recent(self, count: int = 10) -> List[Dict]:
        """View recent activations"""
        metrics = self._load_metrics()
        activations = metrics['activations']
        return activations[-count:]

    def export_report(self, output_file: str = 'docs/activation-report.md'):
        """Export detailed activation report"""
        stats = self.get_stats()
        patterns = self.analyze_patterns()

        report = f"""# Activation Metrics Report

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary Statistics

- **Total Activations:** {stats['total']}
- **Successful:** {stats['successful']}
- **Failed:** {stats['failed']}
- **Success Rate:** {stats['success_rate']}%
- **Average Confidence:** {stats['avg_confidence']}

## Activations by Skill

"""
        for skill, count in sorted(
            stats['by_skill'].items(),
            key=lambda x: x[1],
            reverse=True
        ):
            percentage = (count / stats['total'] * 100) if stats['total'] > 0 else 0
            report += f"- **{skill}**: {count} ({percentage:.1f}%)\n"

        report += f"""

## Most Common Trigger Phrases

"""
        for trigger, count in stats['common_triggers']:
            report += f"- \"{trigger}\": {count} times\n"

        if stats.get('low_confidence_activations'):
            report += f"""

## Low Confidence Activations (< 0.7)

These may need trigger phrase improvements:

"""
            for act in stats['low_confidence_activations']:
                report += (
                    f"- **{act['skill']}**: \"{act['trigger']}\" "
                    f"(confidence: {act['confidence']})\n"
                )

        if patterns['insights']:
            report += f"""

## Insights

"""
            for insight in patterns['insights']:
                report += f"- {insight}\n"

        if patterns['recommendations']:
            report += f"""

## Recommendations

"""
            for rec in patterns['recommendations']:
                report += f"- {rec}\n"

        report += f"""

---

**How to improve:**
1. Add more trigger phrases for underutilized skills
2. Fix failed activations by improving error handling
3. Test with real users to discover missing patterns
4. Adjust confidence thresholds if needed

**Export new report:** `python .claude/skills/_core/tooling/activation_metrics.py export`
"""

        Path(output_file).write_text(report)
        return output_file

    def clear_metrics(self):
        """Clear all metrics (use with caution!)"""
        self._save_metrics(self._init_metrics())

    def _validate_activation_input(
        self,
        skill_name: str,
        trigger_phrase: str,
        confidence: float,
        context: Optional[Dict],
    ) -> float:
        """Validate user-provided activation metadata."""

        if not skill_name or not skill_name.strip():
            raise ValueError('skill name is required')

        if not trigger_phrase or not trigger_phrase.strip():
            raise ValueError('trigger phrase is required')

        try:
            confidence_value = float(confidence)
        except (TypeError, ValueError) as exc:
            raise ValueError('confidence must be a number between 0 and 1') from exc

        if not 0.0 <= confidence_value <= 1.0:
            raise ValueError('confidence must be between 0 and 1')

        if context is not None and not isinstance(context, dict):
            raise ValueError('context must be a dictionary if provided')

        return confidence_value

    def _load_metrics(self) -> Dict:
        """Load metrics from file"""
        if not self.metrics_file.exists():
            return self._init_metrics()

        try:
            with open(self.metrics_file, 'r') as f:
                data = yaml.safe_load(f)
        except Exception:
            return self._init_metrics()

        if not isinstance(data, dict):
            return self._init_metrics()

        data.setdefault('summary', {})
        data.setdefault('activations', [])

        summary = data['summary']
        summary.setdefault('total_activations', 0)
        summary.setdefault('successful_activations', 0)
        summary.setdefault('failed_activations', 0)
        summary.setdefault('by_skill', {})

        return data

    def _save_metrics(self, metrics: Dict):
        """Save metrics to file"""
        with open(self.metrics_file, 'w') as f:
            yaml.dump(metrics, f, default_flow_style=False, sort_keys=False)

    def _init_metrics(self) -> Dict:
        """Initialize empty metrics structure"""
        return {
            'version': '1.0.0',
            'created': datetime.now().isoformat(),
            'summary': {
                'total_activations': 0,
                'successful_activations': 0,
                'failed_activations': 0,
                'by_skill': {}
            },
            'activations': []
        }


def main():
    """CLI interface for metrics system"""
    import sys

    metrics = ActivationMetrics()

    if len(sys.argv) < 2:
        print("Usage: activation_metrics.py [command]")
        print("\nCommands:")
        print("  log <skill> <trigger> <confidence> - Log an activation")
        print("  stats                               - Show statistics")
        print("  analyze                             - Analyze patterns")
        print("  recent [count]                      - Show recent activations")
        print("  export [file]                       - Export detailed report")
        print("  clear                               - Clear all metrics")
        return

    command = sys.argv[1]

    if command == 'log':
        if len(sys.argv) < 5:
            print("Usage: log <skill> <trigger> <confidence>")
            return
        skill = sys.argv[2]
        trigger = sys.argv[3]
        confidence_raw = sys.argv[4]
        try:
            confidence_value = float(confidence_raw)
            metrics.log_activation(skill, trigger, confidence_value)
        except ValueError as exc:
            print(f"❌ Unable to log activation: {exc}")
            return
        print(
            f"✅ Logged: {skill} <- '{trigger}' "
            f"(confidence: {confidence_value:.2f})"
        )

    elif command == 'stats':
        stats = metrics.get_stats()
        print("\n📊 Activation Statistics\n")
        print(f"Total: {stats['total']}")
        print(f"Success Rate: {stats['success_rate']}%")
        print(f"Avg Confidence: {stats['avg_confidence']}\n")
        print("By Skill:")
        for skill, count in sorted(
            stats['by_skill'].items(),
            key=lambda x: x[1],
            reverse=True
        ):
            pct = (count / stats['total'] * 100) if stats['total'] > 0 else 0
            print(f"  {skill}: {count} ({pct:.1f}%)")

    elif command == 'analyze':
        patterns = metrics.analyze_patterns()
        print("\n🔍 Pattern Analysis\n")
        if patterns['insights']:
            print("Insights:")
            for insight in patterns['insights']:
                print(f"  • {insight}")
        print()
        if patterns['recommendations']:
            print("Recommendations:")
            for rec in patterns['recommendations']:
                print(f"  → {rec}")

    elif command == 'recent':
        count = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        recent = metrics.view_recent(count)
        print(f"\n📝 Recent {len(recent)} Activations\n")
        for act in recent:
            status = "✅" if act['success'] else "❌"
            print(
                f"{status} {act['timestamp']} | {act['skill']} | "
                f"'{act['trigger']}' | conf: {act.get('confidence', 'N/A')}"
            )

    elif command == 'export':
        output = sys.argv[2] if len(sys.argv) > 2 else 'docs/activation-report.md'
        report_file = metrics.export_report(output)
        print(f"✅ Report exported to: {report_file}")

    elif command == 'clear':
        confirm = input("Clear all metrics? (yes/no): ")
        if confirm.lower() == 'yes':
            metrics.clear_metrics()
            print("✅ Metrics cleared")
        else:
            print("❌ Cancelled")

    else:
        print(f"Unknown command: {command}")


if __name__ == '__main__':
    main()
