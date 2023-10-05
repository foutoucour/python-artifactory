"""
Import all models here.
"""
from __future__ import annotations

from .artifact import (
    ArtifactFileInfoResponse,
    ArtifactFolderInfoResponse,
    ArtifactInfoResponse,
    ArtifactPropertiesResponse,
    ArtifactStatsResponse,
)
from .auth import AccessTokenModel, ApiKeyModel, AuthModel, PasswordModel
from .group import Group, SimpleGroup
from .permission import Permission, PermissionV2, SimplePermission
from .repository import (
    LocalRepository,
    LocalRepositoryResponse,
    RemoteRepository,
    RemoteRepositoryResponse,
    SimpleRepository,
    VirtualRepository,
    VirtualRepositoryResponse,
)
from .user import BaseUserModel, NewUser, SimpleUser, User, UserResponse

AnyRepositoryResponse = LocalRepositoryResponse | VirtualRepositoryResponse | RemoteRepositoryResponse

AnyRepository = LocalRepository | VirtualRepository | RemoteRepository
AnyPermission = Permission | PermissionV2

__all__ = [
    "ArtifactFileInfoResponse",
    "ArtifactFolderInfoResponse",
    "ArtifactInfoResponse",
    "ArtifactPropertiesResponse",
    "ArtifactStatsResponse",
    "AccessTokenModel",
    "ApiKeyModel",
    "AuthModel",
    "PasswordModel",
    "Group",
    "SimpleGroup",
    "Permission",
    "PermissionV2",
    "SimplePermission",
    "LocalRepository",
    "LocalRepositoryResponse",
    "RemoteRepository",
    "RemoteRepositoryResponse",
    "SimpleRepository",
    "VirtualRepository",
    "VirtualRepositoryResponse",
    "User",
    "UserResponse",
    "BaseUserModel",
    "NewUser",
    "SimpleUser",
    "AnyRepositoryResponse",
    "AnyRepository",
    "AnyPermission",
]
