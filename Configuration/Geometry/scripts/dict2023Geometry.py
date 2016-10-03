maxsections = 5

commonDict = {
    "abbrev" : "O",
    "name" : "common",
    "O1" : {
        1 : [
            'Geometry/CMSCommonData/data/materials.xml',
            'Geometry/CMSCommonData/data/rotations.xml',
            'Geometry/CMSCommonData/data/extend/cmsextent.xml',
            'Geometry/CMSCommonData/data/PostLS2/cms.xml',
            'Geometry/CMSCommonData/data/eta3/etaMax.xml',        
            'Geometry/CMSCommonData/data/cmsMother.xml',
            'Geometry/CMSCommonData/data/cmsTracker.xml',
            'Geometry/CMSCommonData/data/PhaseII/caloBase.xml',
            'Geometry/CMSCommonData/data/cmsCalo.xml',
            'Geometry/CMSCommonData/data/PhaseII/muonBase.xml',
            'Geometry/CMSCommonData/data/cmsMuon.xml',
            'Geometry/CMSCommonData/data/mgnt.xml',
            'Geometry/CMSCommonData/data/PostLS2/beampipe.xml',
            'Geometry/CMSCommonData/data/PostLS2/cmsBeam.xml',
            'Geometry/CMSCommonData/data/muonMB.xml',
            'Geometry/CMSCommonData/data/muonMagnet.xml',
            'Geometry/CMSCommonData/data/cavern.xml',
        ],
        5 : [
            'Geometry/CMSCommonData/data/FieldParameters.xml',
        ],
        "era" : "self.run2_common, self.phase2_common",
    }
}

trackerDict = {
    "abbrev" : "T",
    "name" : "tracker",
    "T1" : {
        1 : [
            'Geometry/TrackerCommonData/data/PhaseII/trackerParameters.xml',
            'Geometry/TrackerCommonData/data/pixfwdCommon.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdMaterials.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdCylinder.xml', 
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwd.xml', 
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdDisks.xml', 
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdInnerDisk1.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdInnerDisk2.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdInnerDisk3.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdInnerDisk4.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdInnerDisk5.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdInnerDisk6.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdInnerDisk7.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdOuterDisk1.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdOuterDisk2.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdOuterDisk3.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdOuterDisk4.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdOuterDisk5.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdOuterDisk6.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdOuterDisk7.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdOuterDisk8.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdOuterDisk9.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdOuterDisk10.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdblade1.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdblade2.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdblade3.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdblade4.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdblade5.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdblade6.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdblade7.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdblade8.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdblade9.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdblade10.xml',
            'Geometry/TrackerCommonData/data/PhaseI/pixbarmaterial.xml', 
            'Geometry/TrackerCommonData/data/PhaseI/pixbarladder.xml', 
            'Geometry/TrackerCommonData/data/PhaseI/pixbarladderfull0.xml', 
            'Geometry/TrackerCommonData/data/PhaseI/pixbarladderfull1.xml', 
            'Geometry/TrackerCommonData/data/PhaseI/pixbarladderfull2.xml', 
            'Geometry/TrackerCommonData/data/PhaseI/pixbarladderfull3.xml', 
            'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer.xml', 
            'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer0.xml', 
            'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer1.xml', 
            'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer2.xml', 
            'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer3.xml', 
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixbar.xml', 
            'Geometry/TrackerCommonData/data/trackermaterial.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/tracker.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/trackerbar.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/trackerfwd.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/trackerStructureTopology.xml',
            'Geometry/TrackerSimData/data/PhaseII/TiltedTracker/trackersens.xml',
            'Geometry/TrackerRecoData/data/PhaseII/TiltedTracker/trackerRecoMaterial.xml',
            'Geometry/TrackerSimData/data/PhaseII/TiltedTracker/trackerProdCuts.xml',
            'Geometry/TrackerSimData/data/trackerProdCutsBEAM.xml',
        ],
        "sim" : [
            'from Geometry.TrackerNumberingBuilder.trackerNumberingGeometry_cfi import *',
        ],
        "reco" : [
            'from Geometry.CommonDetUnit.globalTrackingGeometry_cfi import *',
            'from RecoTracker.GeometryESProducer.TrackerRecoGeometryESProducer_cfi import *',
            'from Geometry.TrackerGeometryBuilder.trackerParameters_cfi import *',
            'from Geometry.TrackerNumberingBuilder.trackerTopology_cfi import *',
            'from Geometry.TrackerGeometryBuilder.idealForDigiTrackerGeometry_cff import *',
            'trackerGeometry.applyAlignment = cms.bool(False)',
        ],
        "era" : "self.phase2_tracker, self.trackingPhase2PU140",
    },
    "T2" : {
        1 : [
            'Geometry/TrackerCommonData/data/PhaseII/trackerParameters.xml',
            'Geometry/TrackerCommonData/data/pixfwdCommon.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdMaterials.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdCylinder.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwd.xml', 
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdDisks.xml', 
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdInnerDisk1.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdInnerDisk2.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdInnerDisk3.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdInnerDisk4.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdInnerDisk5.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdInnerDisk6.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdInnerDisk7.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdOuterDisk1.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdOuterDisk2.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdOuterDisk3.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdOuterDisk4.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdOuterDisk5.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdOuterDisk6.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdOuterDisk7.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdOuterDisk8.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdOuterDisk9.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdOuterDisk10.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdblade1.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdblade2.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdblade3.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdblade4.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdblade5.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdblade6.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdblade7.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdblade8.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdblade9.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdblade10.xml',
            'Geometry/TrackerCommonData/data/PhaseI/pixbarmaterial.xml', 
            'Geometry/TrackerCommonData/data/PhaseI/pixbarladder.xml', 
            'Geometry/TrackerCommonData/data/PhaseI/pixbarladderfull0.xml', 
            'Geometry/TrackerCommonData/data/PhaseI/pixbarladderfull1.xml', 
            'Geometry/TrackerCommonData/data/PhaseI/pixbarladderfull2.xml', 
            'Geometry/TrackerCommonData/data/PhaseI/pixbarladderfull3.xml', 
            'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer.xml', 
            'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer0.xml', 
            'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer1.xml', 
            'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer2.xml', 
            'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer3.xml', 
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixbar.xml', 
            'Geometry/TrackerCommonData/data/trackermaterial.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/tracker.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/trackerbar.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/trackerfwd.xml',
            'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/trackerStructureTopology.xml',
            'Geometry/TrackerSimData/data/PhaseII/FlatTracker/trackersens.xml',
            'Geometry/TrackerRecoData/data/PhaseII/FlatTracker/trackerRecoMaterial.xml',
            'Geometry/TrackerSimData/data/PhaseII/FlatTracker/trackerProdCuts.xml',
            'Geometry/TrackerSimData/data/trackerProdCutsBEAM.xml',
        ],
        "sim" : [
            'from Geometry.TrackerNumberingBuilder.trackerNumberingGeometry_cfi import *',
        ],
        "reco" : [
            'from Geometry.CommonDetUnit.globalTrackingGeometry_cfi import *',
            'from RecoTracker.GeometryESProducer.TrackerRecoGeometryESProducer_cfi import *',
            'from Geometry.TrackerGeometryBuilder.trackerParameters_cfi import *',
            'from Geometry.TrackerNumberingBuilder.trackerTopology_cfi import *',
            'from Geometry.TrackerGeometryBuilder.idealForDigiTrackerGeometry_cff import *',
            'trackerGeometry.applyAlignment = cms.bool(False)',
        ],
        "era" : "self.phase2_tracker, self.trackingPhase2PU140",
    },
    "T3" : {
        1 : [
            'Geometry/TrackerCommonData/data/PhaseII/trackerParameters.xml',
            'Geometry/TrackerCommonData/data/pixfwdCommon.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker4021/pixfwdMaterials.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker4021/pixfwdCylinder.xml', 
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker4021/pixfwd.xml', 
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker4021/pixbar.xml', 
            'Geometry/TrackerCommonData/data/trackermaterial.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker4021/tracker.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker4021/pixel.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker4021/trackerbar.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker4021/trackerfwd.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker4021/trackerStructureTopology.xml',
            'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker4021/pixelStructureTopology.xml',
            'Geometry/TrackerSimData/data/PhaseII/TiltedTracker4021/trackersens.xml',
            'Geometry/TrackerSimData/data/PhaseII/TiltedTracker4021/pixelsens.xml',
            'Geometry/TrackerRecoData/data/PhaseII/TiltedTracker4021/trackerRecoMaterial.xml',
            'Geometry/TrackerRecoData/data/PhaseII/TiltedTracker4021/pixelRecoMaterial.xml',
            'Geometry/TrackerSimData/data/PhaseII/TiltedTracker4021/trackerProdCuts.xml',
            'Geometry/TrackerSimData/data/PhaseII/TiltedTracker4021/pixelProdCuts.xml',
            'Geometry/TrackerSimData/data/trackerProdCutsBEAM.xml',
        ],
        "sim" : [
            'from Geometry.TrackerNumberingBuilder.trackerNumberingGeometry_cfi import *',
        ],
        "reco" : [
            'from Geometry.CommonDetUnit.globalTrackingGeometry_cfi import *',
            'from RecoTracker.GeometryESProducer.TrackerRecoGeometryESProducer_cfi import *',
            'from Geometry.TrackerGeometryBuilder.trackerParameters_cfi import *',
            'from Geometry.TrackerNumberingBuilder.trackerTopology_cfi import *',
            'from Geometry.TrackerGeometryBuilder.idealForDigiTrackerGeometry_cff import *',
            'trackerGeometry.applyAlignment = cms.bool(False)',
        ],
        "era" : "self.phase2_tracker, self.trackingPhase2PU140",
    }   
}

caloDict = {
    "abbrev" : "C",
    "name" : "calo",
    "C1" : {
        1: [
            'Geometry/EcalCommonData/data/PhaseII/ShortEE/eregalgo.xml',
            'Geometry/EcalCommonData/data/ebalgo.xml',
            'Geometry/EcalCommonData/data/ebcon.xml',
            'Geometry/EcalCommonData/data/ebrot.xml',
            'Geometry/EcalCommonData/data/eecon.xml',
            'Geometry/EcalCommonData/data/PhaseII/ShortEE/eefixed.xml',
            'Geometry/EcalCommonData/data/PhaseII/ShortEE/eehier.xml',
            'Geometry/EcalCommonData/data/eealgo.xml',
            'Geometry/EcalCommonData/data/escon.xml',
            'Geometry/EcalCommonData/data/esalgo.xml',
            'Geometry/EcalCommonData/data/eeF.xml',
            'Geometry/EcalCommonData/data/eeB.xml',
            'Geometry/EcalCommonData/data/ectkcable.xml',
            'Geometry/HcalCommonData/data/hcalrotations.xml',
            'Geometry/HcalCommonData/data/PhaseII/hcalalgo.xml',
            'Geometry/HcalCommonData/data/hcalcablealgo.xml',
            'Geometry/HcalCommonData/data/hcalbarrelalgo.xml',
            'Geometry/HcalCommonData/data/PhaseII/hcalendcapalgo.xml',
            'Geometry/HcalCommonData/data/hcalouteralgo.xml',
            'Geometry/HcalCommonData/data/hcalforwardalgo.xml',
            'Geometry/HcalCommonData/data/Run2/hcalSimNumbering16a.xml',
            'Geometry/HcalCommonData/data/Run2/hcalRecNumbering16a.xml',
            'Geometry/HcalCommonData/data/average/hcalforwardmaterial.xml',
        ],
        3 : [
            'Geometry/EcalSimData/data/ecalsens.xml',
            'Geometry/HcalCommonData/data/Phase0/hcalsenspmf.xml',
            'Geometry/HcalSimData/data/hf.xml',
            'Geometry/HcalSimData/data/hfpmt.xml',
            'Geometry/HcalSimData/data/hffibrebundle.xml',
            'Geometry/HcalSimData/data/CaloUtil.xml',
        ],
        4 : [
            'Geometry/HcalSimData/data/HcalProdCuts.xml',
            'Geometry/EcalSimData/data/EcalProdCuts.xml',
            'Geometry/EcalSimData/data/ESProdCuts.xml',
        ],
        "sim" : [
            'from Geometry.HcalCommonData.hcalParameters_cfi      import *',
            'from Geometry.HcalCommonData.hcalDDDSimConstants_cfi import *',
        ],
        "reco" : [
            'from Geometry.CaloEventSetup.CaloTopology_cfi import *',
            'from Geometry.CaloEventSetup.CaloGeometryBuilder_cfi import *',
            'CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",',
            '    SelectedCalos = cms.vstring("HCAL"          ,',
            '                                "ZDC"           ,',
            '                                "EcalBarrel"    ,',
            '                                "EcalEndcap"    ,',
            '                                "TOWER"           )',
            ')',
            'from Geometry.EcalAlgo.EcalBarrelGeometry_cfi import *',
            'from Geometry.EcalAlgo.EcalEndcapGeometry_cfi import *',
            'from Geometry.HcalEventSetup.HcalGeometry_cfi import *',
            'from Geometry.HcalEventSetup.CaloTowerGeometry_cfi import *',
            'from Geometry.HcalEventSetup.CaloTowerTopology_cfi import *',
            'from Geometry.HcalCommonData.hcalDDDRecConstants_cfi import *',
            'from Geometry.HcalEventSetup.hcalTopologyIdeal_cfi import *',
            'from Geometry.CaloEventSetup.EcalTrigTowerConstituents_cfi import *',
            'from Geometry.EcalMapping.EcalMapping_cfi import *',
            'from Geometry.EcalMapping.EcalMappingRecord_cfi import *',
        ],
    },
    "C2" : {
        1 : [
            'Geometry/EcalCommonData/data/ectkcable.xml',
            'Geometry/EcalCommonData/data/PhaseII/eregalgo.xml',
            'Geometry/EcalCommonData/data/ebalgo.xml',
            'Geometry/EcalCommonData/data/ebcon.xml',
            'Geometry/EcalCommonData/data/ebrot.xml',
            'Geometry/EcalCommonData/data/eecon.xml',
            'Geometry/EcalCommonData/data/PhaseII/escon.xml',
            'Geometry/EcalCommonData/data/PhaseII/esalgo.xml',
            'Geometry/HcalCommonData/data/hcalrotations.xml',
            'Geometry/HcalCommonData/data/PhaseII/HGCal/hcalalgo.xml',
            'Geometry/HcalCommonData/data/hcalbarrelalgo.xml',
            'Geometry/HcalCommonData/data/PhaseII/HGCal/hcalendcapalgo.xml',
            'Geometry/HcalCommonData/data/hcalouteralgo.xml',
            'Geometry/HcalCommonData/data/hcalforwardalgo.xml',
            'Geometry/HcalCommonData/data/PhaseII/hcalSimNumbering.xml',
            'Geometry/HcalCommonData/data/PhaseII/hcalRecNumberingRebuild.xml',
            'Geometry/HcalCommonData/data/average/hcalforwardmaterial.xml',
            'Geometry/HGCalCommonData/data/v7/hgcal.xml',
            'Geometry/HGCalCommonData/data/v7/hgcalEE.xml',
            'Geometry/HGCalCommonData/data/v7/hgcalHEsil.xml',
            'Geometry/HGCalCommonData/data/v7/hgcalwafer.xml',
            'Geometry/HGCalCommonData/data/v7/hgcalCons.xml',
        ],
        3 : [
            'Geometry/EcalSimData/data/PhaseII/ecalsens.xml',
            'Geometry/HcalCommonData/data/PhaseII/HGCal/hcalsenspmf.xml',
            'Geometry/HcalSimData/data/hf.xml',
            'Geometry/HcalSimData/data/hfpmt.xml',
            'Geometry/HcalSimData/data/hffibrebundle.xml',
            'Geometry/HcalSimData/data/CaloUtil.xml',
            'Geometry/HGCalSimData/data/hgcsensv6.xml',
            'Geometry/HGCalSimData/data/hgccons.xml',
            'Geometry/HGCalSimData/data/hgcProdCuts.xml',
        ],
        4 : [
            'Geometry/HcalSimData/data/HcalProdCuts.xml',
            'Geometry/EcalSimData/data/EcalProdCuts.xml',
        ],
        "sim" : [
            'from Geometry.HcalCommonData.hcalParameters_cfi      import *',
            'from Geometry.HcalCommonData.hcalDDDSimConstants_cfi import *',
            'from Geometry.HGCalCommonData.hgcalV6ParametersInitialization_cfi import *',
            'from Geometry.HGCalCommonData.hgcalV6NumberingInitialization_cfi import *'
        ],
        "reco" : [
            'from Geometry.CaloEventSetup.HGCalV6Topology_cfi import *',
            'from Geometry.HGCalGeometry.HGCalV6GeometryESProducer_cfi import *',
            'from Geometry.CaloEventSetup.CaloTopology_cfi import *',
            'from Geometry.CaloEventSetup.CaloGeometryBuilder_cfi import *',
            'CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",',
            '    SelectedCalos = cms.vstring("HCAL"                   ,',
            '                                "ZDC"                    ,',
            '                                "EcalBarrel"             ,',
            '                                "TOWER"                  ,',
            '                                "HGCalEESensitive"       ,',
            '                                "HGCalHESiliconSensitive" ',
            '    )',
            ')',
            'from Geometry.EcalAlgo.EcalBarrelGeometry_cfi import *',
            'from Geometry.HcalEventSetup.HcalGeometry_cfi import *',
            'from Geometry.HcalEventSetup.CaloTowerGeometry_cfi import *',
            'from Geometry.HcalEventSetup.CaloTowerTopology_cfi import *',
            'from Geometry.HcalCommonData.hcalDDDRecConstants_cfi import *',
            'from Geometry.HcalEventSetup.hcalTopologyIdeal_cfi import *',
            'from Geometry.CaloEventSetup.EcalTrigTowerConstituents_cfi import *',
            'from Geometry.EcalMapping.EcalMapping_cfi import *',
            'from Geometry.EcalMapping.EcalMappingRecord_cfi import *',
        ],
        "era" : "self.phase2_hcal, self.phase2_hgcal",
    }
}

muonDict = {
    "abbrev" : "M",
    "name" : "muon",
    "M1" : {
        1 : [
            'Geometry/MuonCommonData/data/v1/mbCommon.xml',
            'Geometry/MuonCommonData/data/v1/mb1.xml',
            'Geometry/MuonCommonData/data/v1/mb2.xml',
            'Geometry/MuonCommonData/data/v1/mb3.xml',
            'Geometry/MuonCommonData/data/v1/mb4.xml',
            'Geometry/MuonCommonData/data/design/muonYoke.xml',
            'Geometry/MuonCommonData/data/PhaseII/mf.xml',
            'Geometry/MuonCommonData/data/PhaseII/rpcf.xml',
            'Geometry/MuonCommonData/data/PhaseII/gemf.xml',
            'Geometry/MuonCommonData/data/PhaseII/TDR_BaseLine/gem11.xml',
            'Geometry/MuonCommonData/data/PhaseII/TDR_BaseLine/gem21.xml',
            'Geometry/MuonCommonData/data/v2/csc.xml',
            'Geometry/MuonCommonData/data/PhaseII/mfshield.xml',
            'Geometry/MuonCommonData/data/PhaseII/TDR_BaseLine/me0.xml',
        ],
        2 : [
            'Geometry/MuonCommonData/data/PhaseII/muonNumbering.xml',
        ],
        3 : [
            'Geometry/MuonSimData/data/PhaseII/muonSens.xml',
            'Geometry/DTGeometryBuilder/data/dtSpecsFilter.xml',
            'Geometry/CSCGeometryBuilder/data/cscSpecsFilter.xml',
            'Geometry/CSCGeometryBuilder/data/cscSpecs.xml',
            'Geometry/RPCGeometryBuilder/data/PhaseII/RPCSpecs.xml',
            'Geometry/GEMGeometryBuilder/data/GEMSpecsFilter.xml',
            'Geometry/GEMGeometryBuilder/data/v5/GEMSpecs.xml',
        ],
        4 : [
            'Geometry/MuonSimData/data/PhaseII/muonProdCuts.xml',
        ],
        "reco" : [
            'from Geometry.MuonNumbering.muonNumberingInitialization_cfi import *',
            'from RecoMuon.DetLayers.muonDetLayerGeometry_cfi import *',
            'from Geometry.GEMGeometryBuilder.gemGeometry_cfi import *',
            'from Geometry.GEMGeometryBuilder.me0Geometry_cfi import *',
            'from Geometry.CSCGeometryBuilder.idealForDigiCscGeometry_cff import *',
            'from Geometry.DTGeometryBuilder.idealForDigiDtGeometry_cff import *',
        ],
        "era" : "self.phase2_muon, self.run3_GEM",
    }
}

forwardDict = {
    "abbrev" : "F",
    "name" : "forward",
    "F1" : {
        1 : [
            'Geometry/ForwardCommonData/data/v2/forwardshield.xml',
            'Geometry/ForwardCommonData/data/brmrotations.xml',
            'Geometry/ForwardCommonData/data/PostLS2/brm.xml',
            'Geometry/ForwardCommonData/data/zdcmaterials.xml',
            'Geometry/ForwardCommonData/data/lumimaterials.xml',
            'Geometry/ForwardCommonData/data/zdcrotations.xml',
            'Geometry/ForwardCommonData/data/lumirotations.xml',
            'Geometry/ForwardCommonData/data/zdc.xml',
            'Geometry/ForwardCommonData/data/zdclumi.xml',
            'Geometry/ForwardCommonData/data/cmszdc.xml',
        ],
        3 : [
            'Geometry/ForwardCommonData/data/brmsens.xml',
            'Geometry/ForwardSimData/data/zdcsens.xml',
        ],
        4 : [
            'Geometry/ForwardSimData/data/zdcProdCuts.xml',
            'Geometry/ForwardSimData/data/ForwardShieldProdCuts.xml',
        ],
        "reco" :[
            'from Geometry.ForwardGeometry.ForwardGeometry_cfi import *',
        ]
    }
}

allDicts = [ commonDict, trackerDict, caloDict, muonDict, forwardDict ]

detectorVersionDict = {
    ("O1","T1","C1","M1","F1") : "D1",
    ("O1","T2","C1","M1","F1") : "D2",
    ("O1","T1","C2","M1","F1") : "D3",
    ("O1","T3","C2","M1","F1") : "D4"
}

