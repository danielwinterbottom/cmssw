//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Wed Aug 11 09:24:19 2010 by ROOT version 5.22/00d
// from TTree tree/tree
//////////////////////////////////////////////////////////

#ifndef TreeAnalysisHcalNZS_h
#define TreeAnalysisHcalNZS_h

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include <iomanip>

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include "TDirectory.h"
#include "TH1F.h"
#include "TH2.h"
#include "TProfile.h"
#include "TChain.h"
#include "TString.h"

class TreeAnalysisHcalNZS {

public :

  std::string ecalCharIso;
  std::string hcalCharIso;
  std::string dataType;
  std::string L1Seed;
  double      ebNeutIso, eeNeutIso, hhNeutIso;
  double      dRL1Jet;
  int         GoodPVCut;

  //declaration of histograms
  static const int NEtaBins = 12;
  static const int NPBins   = 15; 

  double genPartPBins[NPBins+1], genPartEtaBins[NEtaBins+1];
  TFile *fout;

  TProfile *h_HcalMeanEneVsEta;

  TProfile *h_trackPCaloE11x11H3x3[NEtaBins+1], *h_trackPCaloE9x9H3x3[NEtaBins+1], *h_trackPCaloE7x7H3x3[NEtaBins+1];

  TH1F *h_NPV[2], *h_PVx[2], *h_PVy[2], *h_PVr[2], *h_PVz[2], *h_PVNDOF[2];
  TH2F *h_PVNTracksSumPt[2];
  TH1F *h_PVNTracks[2], *h_PVTracksSumPt[2], *h_PVNTracksWt[2], *h_PVTracksSumPtWt[2];

  TH1F *h_trackP[6],  *h_trackEta[6], *h_trackPhi[6];
  TH1F *h_trackPt[6], *h_trackDxy[6], *h_trackDz[6], *h_trackChiSq[6];

  TH1F *h_trackPhi_2_2[NEtaBins];
  TH1F *h_trackPhi_3_3[NEtaBins];

  TH1F *h_trackPhi_3_Inner[NEtaBins];
  TH1F *h_trackPhi_3_Outer[NEtaBins];

  TH2F *h_eECAL11x11VsHCAL3x3[NEtaBins];

  TH1F *h_meanTrackP[NPBins][NEtaBins];

  TH1F *h_drTrackL1[NPBins][NEtaBins];
    
  TH1F *h_eECAL7x7_Frac[NPBins][NEtaBins],
       *h_eECAL9x9_Frac[NPBins][NEtaBins],
       *h_eECAL11x11_Frac[NPBins][NEtaBins],
       *h_eECAL15x15_Frac[NPBins][NEtaBins],
       *h_eECAL21x21_Frac[NPBins][NEtaBins],
       *h_eECAL25x25_Frac[NPBins][NEtaBins],
       *h_eECAL31x31_Frac[NPBins][NEtaBins];

  TH1F *hh_eECAL7x7_Frac[NEtaBins],
       *hh_eECAL9x9_Frac[NEtaBins],
       *hh_eECAL11x11_Frac[NEtaBins],
       *hh_eECAL15x15_Frac[NEtaBins],
       *hh_eECAL21x21_Frac[NEtaBins],
       *hh_eECAL25x25_Frac[NEtaBins],
       *hh_eECAL31x31_Frac[NEtaBins];

  TH1F *h_eHCAL3x3_Frac[NPBins][NEtaBins],
       *h_eHCAL5x5_Frac[NPBins][NEtaBins],
       *h_eHCAL7x7_Frac[NPBins][NEtaBins];
  TH1F *h_eHCAL3x3_Frac_20Sig[NPBins][NEtaBins],
       *h_eHCAL5x5_Frac_20Sig[NPBins][NEtaBins],
       *h_eHCAL7x7_Frac_20Sig[NPBins][NEtaBins];
  TH1F *h_eHCAL3x3MIP_Frac[NPBins][NEtaBins],
       *h_eHCAL5x5MIP_Frac[NPBins][NEtaBins],
       *h_eHCAL7x7MIP_Frac[NPBins][NEtaBins];
  TH1F *h_eHCAL3x3MIP_Frac_20Sig[NPBins][NEtaBins],
       *h_eHCAL5x5MIP_Frac_20Sig[NPBins][NEtaBins],
       *h_eHCAL7x7MIP_Frac_20Sig[NPBins][NEtaBins];

  TH1F *hh_eHCAL3x3_Frac[NEtaBins],
       *hh_eHCAL5x5_Frac[NEtaBins],
       *hh_eHCAL7x7_Frac[NEtaBins];
  TH1F *hh_eHCAL3x3_Frac_20Sig[NEtaBins],
       *hh_eHCAL5x5_Frac_20Sig[NEtaBins],
       *hh_eHCAL7x7_Frac_20Sig[NEtaBins];

  TH1F *h_eHCAL3x3_eECAL11x11_response[NPBins][NEtaBins],
       *h_eHCAL5x5_eECAL11x11_response[NPBins][NEtaBins],
       *h_eHCAL7x7_eECAL11x11_response[NPBins][NEtaBins];
  TH1F *h_eHCAL3x3_eECAL11x11_responseMIP[NPBins][NEtaBins],
       *h_eHCAL5x5_eECAL11x11_responseMIP[NPBins][NEtaBins],
       *h_eHCAL7x7_eECAL11x11_responseMIP[NPBins][NEtaBins];
  TH1F *h_eHCAL3x3_eECAL11x11_responseInteract[NPBins][NEtaBins],
       *h_eHCAL5x5_eECAL11x11_responseInteract[NPBins][NEtaBins],
       *h_eHCAL7x7_eECAL11x11_responseInteract[NPBins][NEtaBins];

  TH1F *h_eHCAL3x3_eECAL9x9_response[NPBins][NEtaBins],
       *h_eHCAL5x5_eECAL9x9_response[NPBins][NEtaBins],
       *h_eHCAL7x7_eECAL9x9_response[NPBins][NEtaBins];
  TH1F *h_eHCAL3x3_eECAL9x9_responseMIP[NPBins][NEtaBins],
       *h_eHCAL5x5_eECAL9x9_responseMIP[NPBins][NEtaBins],
       *h_eHCAL7x7_eECAL9x9_responseMIP[NPBins][NEtaBins];
  TH1F *h_eHCAL3x3_eECAL9x9_responseInteract[NPBins][NEtaBins],
       *h_eHCAL5x5_eECAL9x9_responseInteract[NPBins][NEtaBins],
       *h_eHCAL7x7_eECAL9x9_responseInteract[NPBins][NEtaBins];

  TH1F *h_eHCAL3x3_eECAL7x7_response[NPBins][NEtaBins],
       *h_eHCAL5x5_eECAL7x7_response[NPBins][NEtaBins],
       *h_eHCAL7x7_eECAL7x7_response[NPBins][NEtaBins];
  TH1F *h_eHCAL3x3_eECAL7x7_responseMIP[NPBins][NEtaBins],
       *h_eHCAL5x5_eECAL7x7_responseMIP[NPBins][NEtaBins],
       *h_eHCAL7x7_eECAL7x7_responseMIP[NPBins][NEtaBins];
  TH1F *h_eHCAL3x3_eECAL7x7_responseInteract[NPBins][NEtaBins],
       *h_eHCAL5x5_eECAL7x7_responseInteract[NPBins][NEtaBins],
       *h_eHCAL7x7_eECAL7x7_responseInteract[NPBins][NEtaBins];


  //===
  TH1F *h_diff_e15x15e11x11[NPBins][NEtaBins],
    *h_diff_e15x15e11x11_20Sig[NPBins][NEtaBins];

  TH1F *h_diff_h7x7h5x5[NPBins][NEtaBins];
  TH1F *h_maxNearP31x31[NPBins][NEtaBins];
        
  TH1F *h_eECAL7x7_Frac_20Sig[NPBins][NEtaBins],
       *h_eECAL9x9_Frac_20Sig[NPBins][NEtaBins],
       *h_eECAL11x11_Frac_20Sig[NPBins][NEtaBins];
  TH1F *h_eHCAL3x3_eECAL11x11_response_20Sig[NPBins][NEtaBins];
  TH1F *h_eHCAL3x3_eECAL11x11_responseMIP_20Sig[NPBins][NEtaBins];
  TH1F *h_eHCAL3x3_eECAL11x11_responseInteract_20Sig[NPBins][NEtaBins];
  TH1F *h_eHCAL3x3_eECAL9x9_response_20Sig[NPBins][NEtaBins];
  TH1F *h_eHCAL3x3_eECAL9x9_responseMIP_20Sig[NPBins][NEtaBins];
  TH1F *h_eHCAL3x3_eECAL9x9_responseInteract_20Sig[NPBins][NEtaBins];
  TH1F *h_eHCAL3x3_eECAL7x7_response_20Sig[NPBins][NEtaBins];
  TH1F *h_eHCAL3x3_eECAL7x7_responseMIP_20Sig[NPBins][NEtaBins];
  TH1F *h_eHCAL3x3_eECAL7x7_responseInteract_20Sig[NPBins][NEtaBins];
  TH1F *h_eHCAL5x5_eECAL11x11_response_20Sig[NPBins][NEtaBins];
  TH1F *h_eHCAL5x5_eECAL11x11_responseMIP_20Sig[NPBins][NEtaBins];
  TH1F *h_eHCAL5x5_eECAL11x11_responseInteract_20Sig[NPBins][NEtaBins];

  TH1F *hh_eECAL7x7_Frac_20Sig[NEtaBins],
       *hh_eECAL9x9_Frac_20Sig[NEtaBins],
       *hh_eECAL11x11_Frac_20Sig[NEtaBins];

  //================================
   TChain          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // Declaration of leaf types
   Int_t                    t_EvtNo;
   Int_t                    t_RunNo;
   Int_t                    t_Lumi;
   Int_t                    t_Bunch;
   std::vector<double>      *PVx;
   std::vector<double>      *PVy;
   std::vector<double>      *PVz;
   std::vector<int>         *PVisValid;
   std::vector<int>         *PVndof;
   std::vector<int>         *PVNTracks;
   std::vector<int>         *PVNTracksWt;
   std::vector<double>      *t_PVTracksSumPt;
   std::vector<double>      *t_PVTracksSumPtWt;
   std::vector<int>         *PVNTracksHP;
   std::vector<int>         *PVNTracksHPWt;
   std::vector<double>      *t_PVTracksSumPtHP;
   std::vector<double>      *t_PVTracksSumPtHPWt;

   Int_t                     t_L1Decision[128];
   std::vector<std::string> *t_L1AlgoNames;
   std::vector<int>         *t_L1PreScale;
   std::vector<double>      *t_L1CenJetPt;
   std::vector<double>      *t_L1CenJetEta;
   std::vector<double>      *t_L1CenJetPhi;
   std::vector<double>      *t_L1FwdJetPt;
   std::vector<double>      *t_L1FwdJetEta;
   std::vector<double>      *t_L1FwdJetPhi;
   std::vector<double>      *t_L1TauJetPt;
   std::vector<double>      *t_L1TauJetEta;
   std::vector<double>      *t_L1TauJetPhi;
   std::vector<double>      *t_L1MuonPt;
   std::vector<double>      *t_L1MuonEta;
   std::vector<double>      *t_L1MuonPhi;
   std::vector<double>      *t_L1IsoEMPt;
   std::vector<double>      *t_L1IsoEMEta;
   std::vector<double>      *t_L1IsoEMPhi;
   std::vector<double>      *t_L1NonIsoEMPt;
   std::vector<double>      *t_L1NonIsoEMEta;
   std::vector<double>      *t_L1NonIsoEMPhi;
   std::vector<double>      *t_L1METPt;
   std::vector<double>      *t_L1METEta;
   std::vector<double>      *t_L1METPhi;

   std::vector<double>      *t_jetPt;
   std::vector<double>      *t_jetEta;
   std::vector<double>      *t_jetPhi;
   std::vector<double>      *t_nTrksJetCalo;
   std::vector<double>      *t_nTrksJetVtx;

   std::vector<double>      *t_trackPAll;
   std::vector<double>      *t_trackEtaAll;
   std::vector<double>      *t_trackPhiAll;
   std::vector<double>      *t_trackPtAll;
   std::vector<double>      *t_trackDxyAll;
   std::vector<double>      *t_trackDzAll;
   std::vector<double>      *t_trackDxyPVAll;
   std::vector<double>      *t_trackDzPVAll;
   std::vector<double>      *t_trackChiSqAll;

   std::vector<double>      *t_trackP;
   std::vector<double>      *t_trackPt;
   std::vector<double>      *t_trackEta;
   std::vector<double>      *t_trackPhi;
   std::vector<double>      *t_trackEcalEta;
   std::vector<double>      *t_trackEcalPhi;
   std::vector<double>      *t_trackHcalEta;
   std::vector<double>      *t_trackHcalPhi;
   std::vector<int>         *t_trackNOuterHits;
   std::vector<int>         *t_NLayersCrossed;
   std::vector<int>         *t_trackHitsTOB;
   std::vector<int>         *t_trackHitsTEC;
   std::vector<int>         *t_trackHitInMissTOB;
   std::vector<int>         *t_trackHitInMissTEC;
   std::vector<int>         *t_trackHitInMissTIB;
   std::vector<int>         *t_trackHitInMissTID;
   std::vector<int>         *t_trackHitInMissTIBTID;
   std::vector<int>         *t_trackHitOutMissTOB;
   std::vector<int>         *t_trackHitOutMissTEC;
   std::vector<int>         *t_trackHitOutMissTIB;
   std::vector<int>         *t_trackHitOutMissTID;
   std::vector<int>         *t_trackHitOutMissTOBTEC;
   std::vector<int>         *t_trackHitInMeasTOB;
   std::vector<int>         *t_trackHitInMeasTEC;
   std::vector<int>         *t_trackHitInMeasTIB;
   std::vector<int>         *t_trackHitInMeasTID;
   std::vector<int>         *t_trackHitOutMeasTOB;
   std::vector<int>         *t_trackHitOutMeasTEC;
   std::vector<int>         *t_trackHitOutMeasTIB;
   std::vector<int>         *t_trackHitOutMeasTID;
   std::vector<double>      *t_trackOutPosOutHitDr;
   std::vector<double>      *t_trackL;
   std::vector<double>      *t_trackDxy;
   std::vector<double>      *t_trackDxyBS;
   std::vector<double>      *t_trackDz;
   std::vector<double>      *t_trackDzBS;
   std::vector<double>      *t_trackDxyPV;
   std::vector<double>      *t_trackDzPV;
   std::vector<double>      *t_trackChiSq;
   std::vector<int>         *t_trackPVIdx;

   std::vector<double>      *t_maxNearP31x31;
   std::vector<double>      *t_maxNearP21x21;
   std::vector<int>         *t_ecalSpike11x11;
   std::vector<double>      *t_e7x7;
   std::vector<double>      *t_e9x9;
   std::vector<double>      *t_e11x11;
   std::vector<double>      *t_e15x15;
   std::vector<double>      *t_e7x7_10Sig;
   std::vector<double>      *t_e9x9_10Sig;
   std::vector<double>      *t_e11x11_10Sig;
   std::vector<double>      *t_e15x15_10Sig;
   std::vector<double>      *t_e7x7_15Sig;
   std::vector<double>      *t_e9x9_15Sig;
   std::vector<double>      *t_e11x11_15Sig;
   std::vector<double>      *t_e15x15_15Sig;
   std::vector<double>      *t_e7x7_20Sig;
   std::vector<double>      *t_e9x9_20Sig;
   std::vector<double>      *t_e11x11_20Sig;
   std::vector<double>      *t_e15x15_20Sig;
   std::vector<double>      *t_e7x7_25Sig;
   std::vector<double>      *t_e9x9_25Sig;
   std::vector<double>      *t_e11x11_25Sig;
   std::vector<double>      *t_e15x15_25Sig;
   std::vector<double>      *t_e7x7_30Sig;
   std::vector<double>      *t_e9x9_30Sig;
   std::vector<double>      *t_e11x11_30Sig;
   std::vector<double>      *t_e15x15_30Sig;

   std::vector<double>      *t_maxNearHcalP3x3;
   std::vector<double>      *t_maxNearHcalP5x5;
   std::vector<double>      *t_maxNearHcalP7x7;
   std::vector<double>      *t_h3x3;
   std::vector<double>      *t_h5x5;
   std::vector<double>      *t_h7x7;
   std::vector<double>      *t_h3x3Sig;
   std::vector<double>      *t_h5x5Sig;
   std::vector<double>      *t_h7x7Sig;
   std::vector<int>         *t_infoHcal;
   Int_t                     t_nTracks;

   // List of branches
   TBranch                  *b_t_EvtNo;
   TBranch                  *b_t_RunNo;
   TBranch                  *b_t_Lumi; 
   TBranch                  *b_t_Bunch;
   TBranch                  *b_PVx;
   TBranch                  *b_PVy;
   TBranch                  *b_PVz;
   TBranch                  *b_PVisValid;
   TBranch                  *b_PVndof; 
   TBranch                  *b_PVNTracks;
   TBranch                  *b_PVNTracksWt;
   TBranch                  *b_t_PVTracksSumPt;
   TBranch                  *b_t_PVTracksSumPtWt;
   TBranch                  *b_PVNTracksHP;
   TBranch                  *b_PVNTracksHPWt;
   TBranch                  *b_t_PVTracksSumPtHP;
   TBranch                  *b_t_PVTracksSumPtHPWt;

   TBranch                  *b_t_L1Decision;
   TBranch                  *b_t_L1AlgoNames;
   TBranch                  *b_t_L1PreScale;
   TBranch                  *b_t_L1CenJetPt;
   TBranch                  *b_t_L1CenJetEta;
   TBranch                  *b_t_L1CenJetPhi;
   TBranch                  *b_t_L1FwdJetPt;
   TBranch                  *b_t_L1FwdJetEta;
   TBranch                  *b_t_L1FwdJetPhi;
   TBranch                  *b_t_L1TauJetPt;
   TBranch                  *b_t_L1TauJetEta;
   TBranch                  *b_t_L1TauJetPhi;
   TBranch                  *b_t_L1MuonPt;
   TBranch                  *b_t_L1MuonEta;
   TBranch                  *b_t_L1MuonPhi;
   TBranch                  *b_t_L1IsoEMPt;
   TBranch                  *b_t_L1IsoEMEta;
   TBranch                  *b_t_L1IsoEMPhi;
   TBranch                  *b_t_L1NonIsoEMPt;
   TBranch                  *b_t_L1NonIsoEMEta;
   TBranch                  *b_t_L1NonIsoEMPhi;
   TBranch                  *b_t_L1METPt;
   TBranch                  *b_t_L1METEta;
   TBranch                  *b_t_L1METPhi;

   TBranch                  *b_t_jetPt;
   TBranch                  *b_t_jetEta;
   TBranch                  *b_t_jetPhi;
   TBranch                  *b_t_nTrksJetCalo;
   TBranch                  *b_t_nTrksJetVtx;

   TBranch                  *b_t_trackPAll;
   TBranch                  *b_t_trackEtaAll;
   TBranch                  *b_t_trackPhiAll;
   TBranch                  *b_t_trackPtAll;
   TBranch                  *b_t_trackDxyAll;
   TBranch                  *b_t_trackDzAll;
   TBranch                  *b_t_trackDxyPVAll;
   TBranch                  *b_t_trackDzPVAll;
   TBranch                  *b_t_trackChiSqAll;

   TBranch                  *b_t_trackP;
   TBranch                  *b_t_trackPt;
   TBranch                  *b_t_trackEta;
   TBranch                  *b_t_trackPhi;
   TBranch                  *b_t_trackEcalEta;
   TBranch                  *b_t_trackEcalPhi;
   TBranch                  *b_t_trackHcalEta;
   TBranch                  *b_t_trackHcalPhi;
   TBranch                  *b_t_trackNOuterHits;
   TBranch                  *b_t_NLayersCrossed;
   TBranch                  *b_t_trackHitsTOB;
   TBranch                  *b_t_trackHitsTEC;
   TBranch                  *b_t_trackHitInMissTOB;
   TBranch                  *b_t_trackHitInMissTEC;
   TBranch                  *b_t_trackHitInMissTIB;
   TBranch                  *b_t_trackHitInMissTID;
   TBranch                  *b_t_trackHitInMissTIBTID;
   TBranch                  *b_t_trackHitOutMissTOB;
   TBranch                  *b_t_trackHitOutMissTEC;
   TBranch                  *b_t_trackHitOutMissTIB;
   TBranch                  *b_t_trackHitOutMissTID;
   TBranch                  *b_t_trackHitOutMissTOBTEC;
   TBranch                  *b_t_trackHitInMeasTOB;
   TBranch                  *b_t_trackHitInMeasTEC;
   TBranch                  *b_t_trackHitInMeasTIB;
   TBranch                  *b_t_trackHitInMeasTID;
   TBranch                  *b_t_trackHitOutMeasTOB;
   TBranch                  *b_t_trackHitOutMeasTEC;
   TBranch                  *b_t_trackHitOutMeasTIB;
   TBranch                  *b_t_trackHitOutMeasTID;
   TBranch                  *b_t_trackOutPosOutHitDr;
   TBranch                  *b_t_trackL;
   TBranch                  *b_t_trackDxy;
   TBranch                  *b_t_trackDxyBS;
   TBranch                  *b_t_trackDz;
   TBranch                  *b_t_trackDzBS;
   TBranch                  *b_t_trackDxyPV;
   TBranch                  *b_t_trackDzPV; 
   TBranch                  *b_t_trackChiSq;
   TBranch                  *b_t_trackPVIdx;

   TBranch                  *b_t_maxNearP31x31;
   TBranch                  *b_t_maxNearP21x21;
   TBranch                  *b_t_ecalSpike11x11;
   TBranch                  *b_t_e7x7;
   TBranch                  *b_t_e9x9;
   TBranch                  *b_t_e11x11;
   TBranch                  *b_t_e15x15;
   TBranch                  *b_t_e7x7_10Sig;
   TBranch                  *b_t_e9x9_10Sig;
   TBranch                  *b_t_e11x11_10Sig;
   TBranch                  *b_t_e15x15_10Sig;
   TBranch                  *b_t_e7x7_15Sig;
   TBranch                  *b_t_e9x9_15Sig;
   TBranch                  *b_t_e11x11_15Sig;
   TBranch                  *b_t_e15x15_15Sig;
   TBranch                  *b_t_e7x7_20Sig;
   TBranch                  *b_t_e9x9_20Sig;
   TBranch                  *b_t_e11x11_20Sig;
   TBranch                  *b_t_e15x15_20Sig;
   TBranch                  *b_t_e7x7_25Sig;
   TBranch                  *b_t_e9x9_25Sig;
   TBranch                  *b_t_e11x11_25Sig;
   TBranch                  *b_t_e15x15_25Sig;
   TBranch                  *b_t_e7x7_30Sig;
   TBranch                  *b_t_e9x9_30Sig;
   TBranch                  *b_t_e11x11_30Sig;
   TBranch                  *b_t_e15x15_30Sig;

   TBranch                  *b_t_maxNearHcalP3x3;
   TBranch                  *b_t_maxNearHcalP5x5;
   TBranch                  *b_t_maxNearHcalP7x7;
   TBranch                  *b_t_h3x3;
   TBranch                  *b_t_h5x5;
   TBranch                  *b_t_h7x7;
   TBranch                  *b_t_h3x3Sig;
   TBranch                  *b_t_h5x5Sig;
   TBranch                  *b_t_h7x7Sig;
   TBranch                  *b_t_infoHcal;
   TBranch                  *b_t_nTracks; 

   TreeAnalysisHcalNZS(TChain *tree, const char *outFileName);
   virtual ~TreeAnalysisHcalNZS();

   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TChain *tree);
   virtual void     Loop(int cut=1);
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);

   double DeltaPhi(double v1, double v2);
   double DeltaR(double eta1, double phi1, double eta2, double phi2);
   void   BookHistograms(const char *outFileName);
};

#endif
