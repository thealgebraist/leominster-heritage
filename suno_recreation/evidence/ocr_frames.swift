import Foundation
import Vision
let root=URL(fileURLWithPath:CommandLine.arguments[1])
let urls=try FileManager.default.contentsOfDirectory(at:root,includingPropertiesForKeys:nil).filter{$0.pathExtension=="jpg"}.sorted{$0.lastPathComponent<$1.lastPathComponent}
var rows:[[String:Any]]=[]
for (i,url) in urls.enumerated() {
 let req=VNRecognizeTextRequest();req.recognitionLevel = .accurate;req.usesLanguageCorrection=false
 try VNImageRequestHandler(url:url).perform([req])
 let texts=(req.results ?? []).compactMap {r -> [String:Any]? in
 guard let s=r.topCandidates(1).first else{return nil}
 return ["text":s.string,"confidence":s.confidence,"y":r.boundingBox.origin.y]
 }
 rows.append(["time":Double(i)*0.5,"texts":texts])
}
try JSONSerialization.data(withJSONObject:rows,options:[.prettyPrinted,.sortedKeys]).write(to:URL(fileURLWithPath:CommandLine.arguments[2]))
