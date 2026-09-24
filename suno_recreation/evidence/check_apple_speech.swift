import Foundation
import Speech
print("authorization=\(SFSpeechRecognizer.authorizationStatus().rawValue)")
for tag in ["en-GB", "en-US"] {
 if let r = SFSpeechRecognizer(locale: Locale(identifier: tag)) {
  print("locale=\(tag) available=\(r.isAvailable) on_device=\(r.supportsOnDeviceRecognition)")
 } else { print("locale=\(tag) unavailable") }
}
