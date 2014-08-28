## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *

## ------------------------------------------------------
#  NOTE: you can use a bunch of core tools of PAT to
#  taylor your PAT configuration; for a few examples
#  uncomment the lines below
## ------------------------------------------------------
from PhysicsTools.PatAlgos.tools.coreTools import *
removeMCMatching(process, ['All'])

## remove certain objects from the default sequence
removeAllPATObjectsBut(process, ['Muons','Electrons'])

# make sure to keep the created objects
process.out.outputCommands += ['keep *_offlinePrimaryVertices_*_*']
process.out.outputCommands += ['keep *_pat*_*_*',]

## let it run
process.p = cms.Path(
   process.patDefaultSequence
   )

## ------------------------------------------------------
#  In addition you usually want to change the following
#  parameters:
## ------------------------------------------------------
#
#local globaltag
#process.GlobalTag.connect = 'sqlite:GR_R_42_V25/export_GR_R_42_V25.db' 
process.GlobalTag.globaltag = 'GR_R_42_V25::All' 

#luminosity
import FWCore.ParameterSet.Config as cms
import PhysicsTools.PythonAnalysis.LumiList as LumiList
myLumis = LumiList.LumiList(filename='Cert_136033-149442_7TeV_Apr21ReReco_Collisions10_JSON_v2.txt').getCMSSWString().split(',')
process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange()
process.source.lumisToProcess.extend(myLumis)

#input file
import FWCore.Utilities.FileUtils as FileUtils
files2010data = FileUtils.loadListFromFile ('Electron2010data_500files_1.txt') 
readFiles = cms.untracked.vstring( *files2010data )
process.source.fileNames = readFiles

process.maxEvents.input = -1                                  ##  (e.g. -1 to run on all events)
#process.maxEvents.input = 1000                               ##  (e.g. -1 to run on all events)
#output file
process.out.fileName = 'file:///data/pattuples2010/Electron/Electron_PAT_data_500files_1.root' ##  (e.g. 'myTuple.root')
