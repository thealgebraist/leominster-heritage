import Foundation
import Vision
import AVFoundation
let input = CommandLine.arguments[1]
let asset = AVURLAsset(url:URL(fileURLWithPath:input))
let gen = AVAssetImageGenerator(asset:asset)
gen.appliesPreferredTrackTransform = true
let dur = CMTimeGetSeconds(asset.duration)
var rows:[[String:Any]]=[]
for t in stride(from:0.25,to:dur,by:0.5) {
 do {
 let cg = try gen.copyCGImage(at:CMTime(seconds:t,preferredTimescale:600),actualTime:nil)
 let req = VNRecognizeTextRequest()
 req.recognitionLevel = .accurate
 req.usesLanguageCorrection = false
 try VNImageRequestHandler(cgImage:cg).perform([req])
 let texts = (req.results ?? []).compactMap { r -> [String:Any]? in
 guard let s=r.topCandidates(1).first else{return nil}
 return ["text":s.string,"confidence":s.confidence,"y":r.boundingBox.origin.y]
 }
 rows.append(["time":t,"texts":texts])
 } catch { print("error: \(error)") }
}
let data=try JSONSerialization.data(withJSONObject:rows,options:[.prettyPrinted,.sortedKeys])
try data.write(to:URL(fileURLWithPath:CommandLine.arguments[2]))
