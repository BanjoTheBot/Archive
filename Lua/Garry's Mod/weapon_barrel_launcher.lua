SWEP.PrintName			= "Barrel Launcher"
SWEP.Author			= "BanjoTheBirb"
SWEP.Instructions			= "Left Click to fire Barrel, Right Click to fire Explosive Barrel."

SWEP.Spawnable = true
SWEP.AdminOnly = false

SWEP.Primary.ClipSize		= -1
SWEP.Primary.DefaultClip	= -1
SWEP.Primary.Automatic		= true
SWEP.Primary.Ammo		= "none"

SWEP.Secondary.ClipSize		= -1
SWEP.Secondary.DefaultClip	= -1
SWEP.Secondary.Automatic	= false
SWEP.Secondary.Ammo		= "none"

SWEP.Weight			= 5
SWEP.AutoSwitchTo		= false
SWEP.AutoSwitchFrom		= false

SWEP.Slot			= 5
SWEP.SlotPos			= 3
SWEP.DrawAmmo			= false
SWEP.DrawCrosshair		= true

SWEP.ViewModel			= "models/weapons/v_rpg.mdl"
SWEP.WorldModel			= "models/weapons/w_rpg.mdl"

SWEP.ShootSound = Sound( "Metal.SawbladeStick" )

function SWEP:PrimaryAttack()
    self:SetNextPrimaryFire( CurTime() + 0.7 )

    self:ThrowBarrel( "models/props_c17/oildrum001.mdl " )
end

function SWEP:SecondaryAttack()
    self:SetNextSecondaryFire( CurTime() + 1.0 )
    
    self:ThrowBarrel( "model_file " )
end

function SWEP:ThrowBarrel( models/props_c17/oildrum001_explosive.mdl )
    local owner = self:GetOwner()

    if ( not owner:IsValid() ) then return end

    self:EmitSound ( self.ShootSound)

    if ( CLIENT ) then return end

    local ent = ents.Create( models/props_c17/oildrum001_explosive.mdl )

    if ( not ent:IsValid() ) then return end

    ent:SetModel( models/props_c17/oildrum001_explosive.mdl )

    local aimvec = owner:GetAimVector()
	local pos = aimvec * 16
	pos:Add( owner:EyePos() )

    ent:SetPos( pos )

    ent:SetAngles( owner:EyeAngles() )
	ent:Spawn()

    local phys = ent:GetPhysicsObject()
	if ( not phys:IsValid() ) then ent:Remove() return end

    aimvec:Mul( 100 )
	aimvec:Add( VectorRand( -10, 10 ) )
	phys:ApplyForceCenter( aimvec )

    cleanup.Add( owner, "props", ent )

    undo.Create( "Thrown_Barrel" )
		undo.AddEntity( ent )
		undo.SetPlayer( owner )
	undo.Finish()

    timer.Simple( 10, function() if ent and ent:IsValid() then ent:Remove() end end )
end
